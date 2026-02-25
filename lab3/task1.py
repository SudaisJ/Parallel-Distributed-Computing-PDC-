from mpi4py import MPI

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if size < 2:
        return
    if rank == 0:
        data = [1, 2, 3, 4, 5]
        print(f"Process 0: Sending {data}")
        
        comm.send(data, dest=1, tag=11)
        modified_data = comm.recv(source=1, tag=12)        
       
        print(f"Process 0: Final array: {modified_data}")
    elif rank == 1:
        data = comm.recv(source=0, tag=11)       
        modified_data = [x * 2 for x in data] 
        comm.send(modified_data, dest=0, tag=12)
if __name__ == "__main__":
    main()