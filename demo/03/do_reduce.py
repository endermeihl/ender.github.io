# -*- coding: utf-8 -*-
from functools import reduce


def add(x, y):
    return x + y


print(reduce(add, [1, 3, 5, 7, 9]))


def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9]))

DIGITS = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}


def char2num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print(str2int('17632'))


def prod(L):
    return reduce(lambda x, y: x * y, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

print("++++++++++++++++++")


def str2float(s):
    i_s = s[0:s.index('.')]
    i_f = s[len(i_s) + 1:]
    return reduce(lambda x, y: x * 10 + y, map(char2num, i_s)) + reduce(
        lambda x, y: x * 10 + y, map(char2num, i_f)) / 10**len(i_f)


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('120.0034'))