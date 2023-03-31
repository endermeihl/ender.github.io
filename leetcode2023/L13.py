# leetcode 13. Roman to Integer
# https://leetcode-cn.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        code = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        for i in range(len(s)):
            if i < len(s) - 1 and code[s[i]] < code[s[i+1]]:
                res -= code[s[i]]
            else:
                res += code[s[i]]
        return res
