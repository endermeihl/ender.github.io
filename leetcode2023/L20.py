# letcode 20. Valid Parentheses
# author: ender
# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets={')':'(','}':'{',']':'['}
        if len(s)%2!=0:
            return False
        for letter in s:
            if len(stack)!=0 and stack[-1]==brackets.get(letter):
                stack.pop()
            else:
                stack.append(letter)
        if len(stack)!=0:
            return False
        return True