# 8. String to Integer (atoi)
# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        if s[0] == '-':
            sign = -1
        else:
            sign = 1
        if s[0] in ['-', '+']:
            s = s[1:]
        res, i = 0, 0
        while i < len(s) and s[i].isdigit():
            res = res * 10 + ord(s[i]) - ord('0')
            i += 1
        return max(-2**31, min(sign * res, 2**31 - 1))
# Compare this snippet from leetcode2023/L8-2.py: