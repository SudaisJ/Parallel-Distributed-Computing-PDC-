from mpi4py import MPI
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

feedback_data = {
    "region": rank,
    "comment": f"Good service in region {rank}",
    "rating": random.randint(1, 5)
}
all_feedback = comm.gather(feedback_data, root=0)

if rank == 0:
    print("Headquarter received all enhanced feedback:")
    for entry in all_feedback:
        print(f"- Region {entry['region']}: Rating {entry['rating']} | {entry['comment']}")
        