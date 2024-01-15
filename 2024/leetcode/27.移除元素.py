#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
import re


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res=0
        l = len(nums)
        n =0 
        while n <l-res: 
            if nums[n]!=val:
                n+=1
                continue
            else:
                for m in range(n,l-res-1):
                    b=nums[m+1]
                    nums[m+1]=nums[m]
                    nums[m]=b
                res+=1
        return l-res


            
# @lc code=end

