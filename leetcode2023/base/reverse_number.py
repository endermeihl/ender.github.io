def reverse_number(n):
    # n is an integer
    # return the reverse of n
    # no use str
    # no use [::-1]
    # no use int()
    while n % 10 == 0:
        n //= 10
    if n < 0:
        return -reverse_number(-n)
    res = 0
    while n > 0:
        res = res * 10 + n % 10
        n //= 10
    return res

print(reverse_number(123))