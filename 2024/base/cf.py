from concurrent import futures
import time
import math
import sys
def calc(val):
    time.sleep(1)
    return math.factorial(val)
def use_threads(num,values):
    t1 = time.time()
    with futures.ThreadPoolExecutor(num) as executor:
        res = executor.map(calc,values)
    t2 = time.time()
    print(f"Time taken: {t2-t1:.2f} seconds")
    return t2-t1
def use_processes(num,values):
    t1 = time.time()
    with futures.ProcessPoolExecutor(num) as executor:
        res = executor.map(calc,values)
    t2 = time.time()
    print(f"Time taken: {t2-t1:.2f} seconds")
    return t2-t1
def main(workers,values):
    print(f"Using {workers} workers for (len(values)) values")
    t_sec = use_threads(workers,values)
    print(f"Theads took {t_sec:.4f} seconds")
    p_sec = use_processes(workers,values)
    print(f"Threads took {p_sec:.4f} seconds")
if __name__ == "__main__":
    workers = int(sys.argv[1])
    values = list(range(1,6))
    main(workers,values)