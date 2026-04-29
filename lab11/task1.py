import pyopencl as cl
import numpy as np

# Step 1: Define matrix size
N, M = 4, 4

# Step 2: Create random matrices
A = np.random.randint(0, 10, (N, M)).astype(np.float32)
B = np.random.randint(0, 10, (N, M)).astype(np.float32)

# Step 3: Set up OpenCL
context = cl.create_some_context()
queue = cl.CommandQueue(context)

# Step 4: Create buffers
mf = cl.mem_flags
A_buf = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=A)
B_buf = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=B)
C_buf = cl.Buffer(context, mf.WRITE_ONLY, A.nbytes)

# Step 5: Kernel for Subtraction (C[id] = A[id] - B[id])
kernel_code = """
__kernel void matrix_sub(__global const float* A, __global const float* B, __global float* C) {
    int id = get_global_id(0);
    C[id] = A[id] - B[id];
}
"""
program = cl.Program(context, kernel_code).build()

# Step 6: Execute and Retrieve
program.matrix_sub(queue, (N * M,), None, A_buf, B_buf, C_buf)
C = np.empty_like(A)
cl.enqueue_copy(queue, C, C_buf)

print("Matrix A - Matrix B (Difference):\n", C)