#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        temp={"(":")","{":"}","[":"]"}
        res=[]
        if len(s)%2!=0:
            return False
        for i in range(len(s)):
            if s[i] in temp:
                res.append(temp[s[i]])
            elif len(res)==0 or res.pop()!=s[i]:
                return False
        if len(res)==0:
            return True
        return False
# @lc code=end

