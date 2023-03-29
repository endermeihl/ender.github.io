# N 字形变换
# Zigzag Conversion
# https://leetcode-cn.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        l = len(s)
        res = [''] * numRows
        i = 0
        while i < l:
            for j in range(numRows):
                if i < l:
                    res[j] += s[i]
                    i += 1
            for j in range(numRows - 2, 0, -1):
                if i < l:
                    res[j] += s[i]
                    i += 1
        return ''.join(res)