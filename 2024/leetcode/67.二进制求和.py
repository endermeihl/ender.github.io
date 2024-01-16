#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = len(a)-1
        m = len(b)-1
        res=""
        temp=0
        while n>=0 and m>=0:
            res=str((int(a[n])+int(b[m])+temp)%2)+res
            temp=int((int(a[n])+int(b[m])+temp)/2)
            n-=1
            m-=1
        while n>=0:
            res=str((int(a[n])+temp)%2)+res
            temp=int((int(a[n])+temp)/2)
            n-=1
        while m>=0:
            res=str((int(b[m])+temp)%2)+res
            temp=int((int(b[m])+temp)/2)
            m-=1
        if temp!=0:
            res="1"+res
        return res
# @lc code=end

