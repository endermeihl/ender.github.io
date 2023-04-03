from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        length = len(nums)
        temp=set()
        nums.sort()
        for i in range(length-3):
            for k in range(i+1,length-2):
                left=k+1
                right=length-1
                while left<right:
                    s=nums[i]+nums[k]+nums[left]+nums[right]
                    if s>target:
                        right-=1
                    elif s<target:
                        left+=1
                    else:
                        temp.add((nums[i],nums[k],nums[left],nums[right]))
                        while left<right and nums[left]==nums[left+1]:
                            left+=1
                        while left<right and nums[right]==nums[right-1]:
                            right-=1
                        left+=1
                        right-=1
        return list(temp)