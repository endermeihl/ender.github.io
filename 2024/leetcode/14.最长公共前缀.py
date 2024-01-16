#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        res=""
        for i in range(len(strs[0])):
            temp=strs[0][0:i+1]
            for j in range(len(strs)):
                if i>len(strs[j]) or temp!=strs[j][0:i+1]:
                    return res
            res=temp
        return res
# @lc code=end

