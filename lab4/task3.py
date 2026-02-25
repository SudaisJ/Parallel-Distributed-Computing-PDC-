from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# PART 1
my_value = rank
gathered = comm.gather(my_value, root=0)
if rank == 0:
    print(f"Gathered: {gathered}")

# PART 2
my_array = np.array([rank], dtype='i')
if rank == 0:
    correct_buffer = np.empty(size, dtype='i')
    try:
        comm.Gather(my_array, None, root=0)
    except:
        print("Buffer Error caught")
else:
    correct_buffer = None

comm.Gather(my_array, correct_buffer, root=0)

# PART 3
my_data = np.array([rank] * (rank + 1), dtype='i')
if rank == 0:
    counts = np.array([r + 1 for r in range(size)], dtype='i')
    disps = np.array([sum(counts[:r]) for r in range(size)], dtype='i')
    recv_buf = np.empty(sum(counts), dtype='i')
else:
    counts = disps = recv_buf = None

comm.Gatherv(my_data, [recv_buf, counts, disps, MPI.INT], root=0)

if rank == 0:
    print(f"Gatherv Result: {recv_buf}")