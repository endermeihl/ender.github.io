#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
from unittest import result


class Solution:
    def romanToInt(self, s: str) -> int:
        nums={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        nums2={'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        result=0
        le=len(s)
        i=0
        while i<le:
            if i+1<le and s[i]+s[i+1] in nums2:
                result+=nums2[s[i]+s[i+1]]
                i+=2
            else:
                result=result+nums[s[i]]
                i+=1
        return result
# @lc code=end

