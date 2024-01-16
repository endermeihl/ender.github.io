#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <0:
            return False
        temp=x
        y=0
        while temp >0:
            y = y*10+temp%10
            temp = int(temp/10)
        if x==y:
            return True
        return False        
# @lc code=end