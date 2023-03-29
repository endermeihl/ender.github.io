# Given a string s, find the length of the longest ubstring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        maxnum =0
        pra = set() # create a set # set() is a function # set function list
        
        for i in range(l):
            if s[i] not in pra:
                pra.add(s[i])
                maxnum=max(maxnum,len(pra))
            else:
                while s[i] in pra:
                    pra.remove(s[i-len(pra)])
                pra.add(s[i])
        return maxnum