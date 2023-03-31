# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/

from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def dfs(index,right,left,temp):
            if index == n*2:
                res.append(temp)
                return
            if left <n:
                dfs(index+1,right,left+1,temp+"(")
            if right < left: # must be right < left not right < n
                dfs(index+1,right+1,left,temp+")")
        
        dfs(0,0,0,"")
        return res