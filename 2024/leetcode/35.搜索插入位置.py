#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=0
        m=len(nums)-1
        if nums[n]>target:
            return n
        if nums[m]<target:
            return m+1
        while n<m and n!=m-1:
            middle=int((n+m)/2)
            if target==nums[middle]:
                return middle
            elif target<nums[middle]:
                m=middle
            else:
                n=middle
        if nums[n]==target:
            return n
        if nums[m]==target:
            return m
        return m
# @lc code=end

