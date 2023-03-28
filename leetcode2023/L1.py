# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s = len(nums)
        for i in range(s):
            for j in range(i + 1, s):
                if nums[i] + nums[j] == target:
                    return [i, j]

        # build a hashmap
        # hashmap = {}
        # for i in range(s):
        #     hashmap[nums[i]] = i
        # for i in range(s):
        #     if target - nums[i] in hashmap and i != hashmap[target - nums[i]]:
        #         return [i, hashmap[target - nums[i]]]
