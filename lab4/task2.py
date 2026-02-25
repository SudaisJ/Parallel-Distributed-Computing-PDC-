from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

data = rank

#   MPI.SUM & MPI.PROD

total_sum = comm.reduce(data, op=MPI.SUM, root=0)

total_prod = comm.reduce(data, op=MPI.PROD, root=0)

if rank == 0:
    print(f"Number of processes: {size}")
    print(f"Result of MPI.SUM: {total_sum}")
    print(f"Result of MPI.PROD: {total_prod}")