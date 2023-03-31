from typing import List

def combine(n: int, k: int) -> List[List[int]]:
    def backtrack(start: int, curr: List[int]):
        if len(curr) == k:
            res.append(curr[:])
            return
        for i in range(start, n+1):
            curr.append(i)
            backtrack(i+1, curr)
            curr.pop()
    
    res = []
    backtrack(1, [])
    return res
