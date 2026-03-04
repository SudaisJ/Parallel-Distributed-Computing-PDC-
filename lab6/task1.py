from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    sales_data = np.arange(size * 4).reshape(size, 4) 
else:
    sales_data = None

recv_sales = np.empty(4, dtype=int) 
comm.Scatter(sales_data, recv_sales, root=0)

print(f"Regional Manager {rank} received monthly sales data: {recv_sales}")