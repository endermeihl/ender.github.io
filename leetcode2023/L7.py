# 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        res=int(s[::-1]) if x >= 0 else int(s[1::][::-1])*-1
        if res >2**31-1 or res <-2**31:
            return 0
        return res