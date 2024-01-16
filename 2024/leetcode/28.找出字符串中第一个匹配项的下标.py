#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        if m > len(haystack):
            return -1
        if m == len(haystack):
            if haystack==needle:
                return 0
            else:
                return -1
        for n in range(0,len(haystack)):
            if haystack[n:n+m]==needle:
                return n
        return -1
# @lc code=end

