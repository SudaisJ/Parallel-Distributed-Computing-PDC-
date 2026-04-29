import pyopencl as cl
import numpy as np

# Dimensions: A(4x2), B(2x3) -> C(4x3)
M, K, N = 4, 2, 3
A = np.random.randint(0, 5, (M, K)).astype(np.float32)
B = np.random.randint(0, 5, (K, N)).astype(np.float32)

# Set up OpenCL context and queue
context = cl.create_some_context()
queue = cl.CommandQueue(context)

# Define memory flags and create buffers
mf = cl.mem_flags
A_buf = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=A)
B_buf = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=B)
C_buf = cl.Buffer(context, mf.WRITE_ONLY, M * N * 4) 

kernel_code = """
__kernel void matrix_mul_non_square(const int M, const int K, const int N,
    __global const float* A, __global const float* B, __global float* C) {
    int row = get_global_id(0); 
    int col = get_global_id(1); 
    
    float sum = 0.0f;
    for (int k = 0; k < K; k++) {
        sum += A[row * K + k] * B[k * N + col];
    }
    C[row * N + col] = sum;
}
"""
program = cl.Program(context, kernel_code).build()

# Note: arguments must match the kernel signature
program.matrix_mul_non_square(queue, (M, N), None, 
                              np.int32(M), np.int32(K), np.int32(N), 
                              A_buf, B_buf, C_buf)

C = np.empty((M, N), dtype=np.float32)
cl.enqueue_copy(queue, C, C_buf)

print("Matrix A (4x2):\n", A)
print("Matrix B (2x3):\n", B)
print("Result C (4x3):\n", C)