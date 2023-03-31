L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print(L[-1:0])

print([x * x for x in range(1, 11) if x % 2])

print([m + n for m in 'ABC' for n in 'XYZ'])

import os

print([d for d in os.listdir('.')])  # os.listdir可以列出文件和目录

g = (x * x for x in range(10))

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


fib(7)

L = [1, 8, 28, 56, 70, 56, 28, 8, 1]
L = [0, *L, 0]
print(L)
print(L[:-1])
L = [a + L[i + 1] for i, a in enumerate(L[:-1])]
print(L)

s = '123.456'
print(s.index('.'))