from mpi4py import MPI
import time
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    jobs = [101, 102, 103, 104, 105, 106]
    worker_count = size - 1
    
    for job in jobs:

        status = MPI.Status()
        worker_rank = comm.recv(source=MPI.ANY_SOURCE, tag=1, status=status)
        comm.send(job, dest=status.Get_source(), tag=2)

    for i in range(1, size):
        comm.send(-1, dest=i, tag=2)
    print("Master: All jobs assigned and completed.")

else:
    while True:
        comm.send(rank, dest=0, tag=1)
        job = comm.recv(source=0, tag=2)
        
        if job == -1:
            break
            
        print(f"Worker {rank}: Processing job {job}...")
        time.sleep(random.uniform(0.5, 1.5)) 