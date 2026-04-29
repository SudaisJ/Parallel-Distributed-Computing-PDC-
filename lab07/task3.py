from mpi4py import MPI
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
local_val = random.randint(10, 100)
print(f"Process {rank} generated value: {local_val}")
min_val = comm.allreduce(local_val, op=MPI.MIN)

print(f"Process {rank} now knows the global minimum is: {min_val}")