from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = ["Hello", "from", "Process", "0"]
    req = comm.isend(data, dest=1)
    print("Process 0 sending:", data)
    req.wait()

elif rank == 1:
    req = comm.irecv(source=0)
    data = req.wait()
    print("Process 1 received:", data)