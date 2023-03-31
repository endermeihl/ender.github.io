from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        le = len(digits)
        if le == 0:
            return []
        code = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        reb = []
        res = []

        def dfs(index:int):
            if len(digits) == index:
                res.append("".join(reb))
            else:
                digit=digits[index]
                for i in code[digit]:
                    reb.append(i)
                    dfs(index + 1)
                    reb.pop()
        dfs(0)
        