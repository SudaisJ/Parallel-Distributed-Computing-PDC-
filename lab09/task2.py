import pyopencl as cl
import numpy as np

# Data
A = np.array([10,20,30,40], dtype=np.float32)
B = np.array([1,2,3,4], dtype=np.float32)

# Handle different sizes
if len(A) != len(B):
    min_size = min(len(A), len(B))
    A = A[:min_size]
    B = B[:min_size]

# OpenCL Setup
platform = cl.get_platforms()[0]
device = platform.get_devices()[0]
context = cl.Context([device])
queue = cl.CommandQueue(context)

# Kernel (SUBTRACTION)
kernel_code = """
__kernel void subtract(
    __global float *A,
    __global float *B,
    __global float *C)
{
    int i = get_global_id(0);
    C[i] = A[i] - B[i];
}
"""

program = cl.Program(context, kernel_code).build()

# Buffers
mf = cl.mem_flags
buf_A = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=A)
buf_B = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=B)
buf_C = cl.Buffer(context, mf.WRITE_ONLY, A.nbytes)

# Run Kernel
program.subtract(queue, A.shape, None, buf_A, buf_B, buf_C)

# Result
C = np.empty_like(A)
cl.enqueue_copy(queue, C, buf_C)

print("Result (A - B):", C)