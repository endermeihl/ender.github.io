#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)-1
        eg = 1
        while n >=0:
            temp=digits[n]
            digits[n]=(digits[n]+eg)%10
            eg = int((temp+eg)/10)
            n-=1
        if eg>0:
            digits = [1] + digits
        return digits
            
# @lc code=end

