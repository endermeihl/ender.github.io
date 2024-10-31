from concurrent import futures
import math
import sys
def calc(val):
    result = math.sqrt(float(val))
    return val,result
def use_threads(num,values):
    with futures.ThreadPoolExecutor(num) as executor:
        tasks = [executor.submit(calc,val) for val in values]
        for f in futures.as_completed(tasks):
            yield f.result()
def use_processes(num,values):
    with futures.ProcessPoolExecutor(num) as executor:
        tasks = [executor.submit(calc,val) for val in values]
        for f in futures.as_completed(tasks):
            yield f.result()
def main(workers,values):
    print(f"Using {workers} workers for {len(values)} values")
    print("Threads:")
    for val,result in use_threads(workers,values):
        print(f'{val}:{result:.4f}')
    print("Processes:")
    for val,result in use_processes(workers,values):
        print(f'{val}:{result:.4f}')
if __name__ == "__main__":
    workers = 3
    if len(sys.argv) > 1:
        workers = int(sys.argv[1])
    values = list(range(1,6))
    main(workers,values)