from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

local_data = [20.0 + rank, 50.0 + rank, 5.0 + rank]

max_vals = comm.reduce(local_data, op=MPI.MAX, root=0)
sum_vals = comm.reduce(local_data, op=MPI.SUM, root=0)

if rank == 0:
    avg_vals = [round(x / size, 2) for x in sum_vals]
    labels = ["Temp", "Humidity", "Wind"]
    
    print(f"{'METRIC':<10} | {'MAX':<8} | {'AVG':<8}")
    print("-" * 30)
    for i in range(len(labels)):
        print(f"{labels[i]:<10} | {max_vals[i]:<8} | {avg_vals[i]:<8}")