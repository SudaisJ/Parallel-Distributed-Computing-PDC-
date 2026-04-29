from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

data_chunks = [
    "hello world mpi",
    "distributed computing is fun",
    "mpi reduce is powerful",
    "learning mpi with python"
]

local_text = data_chunks[rank] if rank < len(data_chunks) else ""
local_count = len(local_text.split())

total_words = comm.reduce(local_count, op=MPI.SUM, root=0)

if rank == 0:
    print(f"Total distributed word count: {total_words}")