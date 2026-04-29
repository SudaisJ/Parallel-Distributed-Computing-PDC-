from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    data = np.array([10, 20, 30, 40], dtype='i')
    print(f"Original Array: {data}")
    chunk_size = len(data) // size
else:
    data = None
    chunk_size = None

chunk_size = comm.bcast(chunk_size, root=0)
recv_box = np.empty(chunk_size, dtype='i')

comm.Scatter(data, recv_box, root=0)

doubled = recv_box * 2

result = np.empty(size * chunk_size, dtype='i') if rank == 0 else None
comm.Gather(doubled, result, root=0)

if rank == 0:
    print(f"Modified Array: {result}")