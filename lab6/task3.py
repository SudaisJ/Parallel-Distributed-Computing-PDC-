from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

revenue = (rank + 1) * 15000 

all_revenues = comm.gather(revenue, root=0)

if rank == 0:
    all_revenues.sort()
    median_revenue = np.median(all_revenues)
    print(f"All revenues: {all_revenues}")
    print(f"Median revenue among branches: ${median_revenue}")