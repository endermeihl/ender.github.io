def subsets(nums):
    result = []
    n = len(nums)

    def backtrack(start, path): # start: the index of the first element to be added
        result.append(path)

        for i in range(start, n):
            backtrack(i + 1, path + [nums[i]])

    backtrack(0, [])
    return result
# Path: leetcode2023/base/subsets.py