from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

value = rank + 2
prefix_prod = comm.scan(value, op=MPI.PROD)

print(f"Process {rank}: Cumulative Product = {prefix_prod}")