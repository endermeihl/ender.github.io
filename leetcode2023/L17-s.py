from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        if not digits:
            return res
        code = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
       
        def dfs(index,temp):
            if index == len(digits):
                res.append(temp)
                return
            for n in code[digits[index]]:
                dfs(index+1,temp+n)
        dfs(0,"")
        return res