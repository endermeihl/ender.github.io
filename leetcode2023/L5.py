def longestPalindrome(s)->str:
    max_len = 0
    max_str = ''
    l = len(s)
    for i in range(l):
        for j in range(i+1,l+1):
            if is_palindrome(s[i:j]) and j-i > max_len:
                max_len = j-i
                max_str = s[i:j]
    return max_str

def is_palindrome(s):
    if len(s) < 2:
        return True
    return s == s[::-1] # [::-1] means reverse the string