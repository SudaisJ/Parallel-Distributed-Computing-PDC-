from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data_to_send = 42
    print(f"Process 0: Sending data {data_to_send} to Process 1...")
    req = comm.isend(data_to_send, dest=1, tag=11)
    req.wait()
    print("Process 0: Send complete.")

elif rank == 1:
    req = comm.irecv(source=0, tag=11)
    print("Process 1: Doing heavy computation while waiting for data...")
    result = 0
    for i in range(10**6):
        result += i
    print(f"Process 1: Computation finished (Result: {result}). Now checking for data.")
    received_data = req.wait()
    print(f"Process 1: Finally received data: {received_data}")