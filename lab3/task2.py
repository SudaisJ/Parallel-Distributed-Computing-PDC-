from mpi4py import MPI
import time

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if size < 2:
        return

    if rank == 0:
        message = "Hello from Process 0"
        req = comm.isend(message, dest=1, tag=11)
        req.wait()

    elif rank == 1:
        req = comm.irecv(source=0, tag=11)
        
        for i in range(5):
            print(f"Process 1: Performing parallel computation step {i+1}...")
            time.sleep(0.5)
            
        message = req.wait()
        print(f"Process 1: Received message: {message}")

if __name__ == "__main__":
    main()