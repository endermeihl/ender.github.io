# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x1 = int(str(x)[::-1])
        if x1 == x:
            return True
        return False