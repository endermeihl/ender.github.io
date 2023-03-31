# 16. 3Sum Closest
# https://leetcode.com/problems/3sum-closest/

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        le = len(nums)
        res = nums[0]+nums[1]+nums[2]
        maxb = abs(target-res)
        nums.sort()
        if le == 3:
            return res
        for i in range(le):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = le - 1
            while left < right:
                s = nums[i]+nums[left]+nums[right]
                dif = abs(target-s)
                if maxb > dif:
                    res = s
                    maxb = dif
                if s > target:
                    right -= 1
                elif s < target:
                    left += 1
                else:
                    return res
        return res
