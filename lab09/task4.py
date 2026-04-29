import pyopencl as cl
import numpy as np

# Input vectors
A = np.array([2, 4, 6, 8], dtype=np.float32)
B = np.array([1, 3, 5, 7], dtype=np.float32)

# OpenCL setup
platform = cl.get_platforms()[0]
device = platform.get_devices()[0]
context = cl.Context([device])
queue = cl.CommandQueue(context)

# OpenCL Kernel
kernel_code = """
__kernel void temp_multiply(
    __global float *A,
    __global float *B,
    __global float *temp)
{
    int i = get_global_id(0);
    temp[i] = A[i] * B[i];
}
"""

# Build program
program = cl.Program(context, kernel_code).build()

# Buffers
mf = cl.mem_flags
buf_A = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=A)
buf_B = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=B)
temp_buf = cl.Buffer(context, mf.WRITE_ONLY, A.nbytes)

# Execute kernel
program.temp_multiply(queue, A.shape, None,
                      buf_A, buf_B, temp_buf)

# Copy result
temp = np.empty_like(A)
cl.enqueue_copy(queue, temp, temp_buf)

print("Vector A:", A)
print("Vector B:", B)
print("Temporary Array Result:", temp)