def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(3))


def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)

move(3,'A' ,'B' ,'C')
