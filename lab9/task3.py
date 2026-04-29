import pyopencl as cl
import numpy as np

# Input vectors
A = np.array([1, 2, 3, 4], dtype=np.float32)
B = np.array([5, 6, 7, 8], dtype=np.float32)

# OpenCL setup
platform = cl.get_platforms()[0]
device = platform.get_devices()[0]
context = cl.Context([device])
queue = cl.CommandQueue(context)

# OpenCL Kernel
kernel_code = """
__kernel void multiply(
    __global float *A,
    __global float *B,
    __global float *C)
{
    int i = get_global_id(0);
    C[i] = A[i] * B[i];
}
"""

# Build program
program = cl.Program(context, kernel_code).build()

# Memory buffers
mf = cl.mem_flags
buf_A = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=A)
buf_B = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=B)
buf_C = cl.Buffer(context, mf.WRITE_ONLY, A.nbytes)

# Execute kernel
program.multiply(queue, A.shape, None, buf_A, buf_B, buf_C)

# Get result
C = np.empty_like(A)
cl.enqueue_copy(queue, C, buf_C)

print("Vector A:", A)
print("Vector B:", B)
print("Element-wise Multiplication Result:", C)