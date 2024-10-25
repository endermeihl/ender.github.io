def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)
    
print(power(2, 0))


def search(sequence, number, lower, upper):
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle + 1, upper)
        else:
            return search(sequence, number, lower, middle)