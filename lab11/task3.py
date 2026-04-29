import pyopencl as cl
import numpy as np

# Step 1: Define dimensions (N rows, M columns)
N, M = 3, 5 
A = np.random.randint(0, 10, (N, M)).astype(np.float32)

# Step 2: Set up OpenCL context and queue[cite: 1]
# Note: This will prompt you to select a device (CPU/GPU) in the terminal
context = cl.create_some_context()
queue = cl.CommandQueue(context)

# Step 3: Create memory buffers[cite: 1]
mf = cl.mem_flags
A_buf = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=A)
T_buf = cl.Buffer(context, mf.WRITE_ONLY, A.nbytes)

# Step 4: Write OpenCL kernel for Transpose[cite: 1]
kernel_code = """
__kernel void matrix_transpose(const int N, const int M, __global const float* A, __global float* T) {
    int row = get_global_id(0); // Row index of A
    int col = get_global_id(1); // Column index of A
    
    // Check bounds to prevent illegal memory access
    if (row < N && col < M) {
        // Formula: T[col][row] = A[row][col][cite: 1]
        T[col * N + row] = A[row * M + col];
    }
}
"""
program = cl.Program(context, kernel_code).build()

# Step 5: Execute kernel[cite: 1]
# Global work size matches the dimensions of matrix A (N, M)
program.matrix_transpose(queue, (N, M), None, np.int32(N), np.int32(M), A_buf, T_buf)

# Step 6: Retrieve result[cite: 1]
T = np.empty((M, N), dtype=np.float32)
cl.enqueue_copy(queue, T, T_buf)

# Step 7: Display results[cite: 1]
print("Original Matrix (3x5):\n", A)
print("\nTransposed Matrix (5x3):\n", T)