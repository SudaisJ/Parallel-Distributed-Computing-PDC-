from mpi4py import MPI


comm = MPI.COMM_WORLD
rank = comm.Get_rank()

value = rank + 2 
product_result = comm.reduce(value, op=MPI.PROD, root=0)
if rank == 0:
    print(f" GLOBAL REDUCTION COMPLETE ")
    print(f"Total Product of all branches: {product_result}")
   