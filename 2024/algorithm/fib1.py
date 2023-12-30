def fib1(n:int) -> int:
    print(f"fib1({n}) is called")
    if n < 2:# base case
        return n
    return fib1(n-1) + fib1(n-2) # recursive case

if __name__ == "__main__":
    print(fib1(5))
    print(fib1(10))