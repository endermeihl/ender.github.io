from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]
        le = len(nums)
        if le < 4:
            return res
        for i in range(le-3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1,le-2):
                if j > i+1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = le - 1
                while left < right:
                    s = nums[i]+nums[j]+nums[left]+nums[right]
                    if s > target:
                        right -= 1
                    elif s < target:
                        left += 1
                    else:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
        return res