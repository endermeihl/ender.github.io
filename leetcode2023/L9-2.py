class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        if x % 10 == 0 and x != 0: return False
        cur = 0
        num = x
        while num != 0:
            cur = cur * 10 + num % 10
            num //= 10
        return cur == x