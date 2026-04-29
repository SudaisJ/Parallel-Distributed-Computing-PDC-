import pyopencl as cl
import numpy as np
import time

N = 1024
A = np.random.rand(N, N).astype(np.float32)
B = np.random.rand(N, N).astype(np.float32)

start_time = time.time()
C_cpu = np.dot(A, B)
cpu_duration = time.time() - start_time
print(f"NumPy Execution Time: {cpu_duration:.4f} seconds")

context = cl.create_some_context()
queue = cl.CommandQueue(context)

# Step 3: Define memory flags and create buffers
mf = cl.mem_flags 
A_buf = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=A)
B_buf = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=B)
C_buf = cl.Buffer(context, mf.WRITE_ONLY, A.nbytes)

kernel_code = """
__kernel void matrix_mul(const int N, __global const float* A, __global const float* B, __global float* C) {
    int row = get_global_id(0); 
    int col = get_global_id(1);
    float sum = 0.0f;
    for (int k = 0; k < N; k++) { 
        sum += A[row * N + k] * B[k * N + col]; 
    }
    C[row * N + col] = sum;
}
"""
program = cl.Program(context, kernel_code).build()

start_time = time.time()
program.matrix_mul(queue, (N, N), None, np.int32(N), A_buf, B_buf, C_buf)
queue.finish() # Crucial: Wait for the GPU to actually finish[cite: 1]
gpu_duration = time.time() - start_time
print(f"OpenCL Execution Time: {gpu_duration:.4f} seconds")

if gpu_duration < cpu_duration:
    print(f"GPU is {cpu_duration / gpu_duration:.2f}x faster than CPU.")