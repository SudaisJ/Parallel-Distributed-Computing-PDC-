from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    for i in range(5):
        msg = f"Log {i} from Process 0"
        req = comm.isend(msg, dest=1)
        req.wait()
        print("Sent:", msg)
        time.sleep(1)

elif rank == 1:
    for i in range(5):
        req = comm.irecv(source=0)
        msg = req.wait()
        print("Received:", msg)

       