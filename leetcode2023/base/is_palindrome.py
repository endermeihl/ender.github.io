def is_palindrome(s):
    if len(s) < 2:
        return True
    return s == s[::-1] # [::-1] means reverse the string