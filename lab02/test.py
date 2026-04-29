from mpi4py import MPI

def main():
    # Get the global communicator
    comm = MPI.COMM_WORLD
    
    # Get the total number of processes
    size = comm.Get_size()
    
    # Get the rank (ID) of the current process
    rank = comm.Get_rank()
    
    # Each process prints its info
    print(f"Hello from rank {rank} out of {size} total processes.")

    # Simple data sharing example: Rank 0 sends data to others
    if rank == 0:
        data = {'key1': [7, 2.72, 2+3j], 'key2': ('abc', 'xyz')}
        print(f"Rank 0 is broadcasting data: {data}")
    else:
        data = None

    # Broadcast the data from rank 0 to all other ranks
    data = comm.bcast(data, root=0)
    
    print(f"Rank {rank} received data: {data}")

if __name__ == "__main__":
    main()