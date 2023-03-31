from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        le = len(digits)
        if le ==0:
            return []
        code={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res=[]
        for n in digits:
            if len(res)==0:
                res=code[n]
                continue
            f = []
            for i in res:
               for j in code[n]:
                   f.append(i+j)
            res = f
        return res