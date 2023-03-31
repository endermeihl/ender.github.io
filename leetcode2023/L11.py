# leetcode 11
# https://leetcode-cn.com/problems/container-with-most-water/
# 11. 盛最多水的容器

from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0 
        left = 0
        right = len(height)-1
        while left < right:
            if height[left] <= height[right]:
                res = max(res,(right-left)*height[left])
                left+=1
            else:
                res = max(res,(right-left)*height[right])
                right-=1
        return res