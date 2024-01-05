# memoization 结果缓存
# 递归调用的结果缓存，避免重复计算
# 递归调用的时间复杂度为 O(2^n)
# 递归调用的空间复杂度为 O(n)
from typing import Dict
memo: Dict[int, int] = {0:0, 1:1} # base case

def fib3(n:int) -> int:
    print(f"fib1({n}) is called")
    if n not in memo:
        memo[n] = fib3(n-1) + fib3(n-2) # recursive case
    return memo[n]

if __name__ == "__main__":
    print(fib3(50))