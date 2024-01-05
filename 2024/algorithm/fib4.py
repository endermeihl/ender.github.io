# 自动化的结果缓存

from functools import lru_cache
@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    print(f"fib4({n}) is called")
    if n < 2: # base case
        return n
    return fib4(n-2) + fib4(n-1)

if __name__ == "__main__":
    fib4(50)