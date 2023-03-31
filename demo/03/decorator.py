# -*- coding: utf-8 -*-

import time, functools


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        startime = time.time()
        result = fn(*args, **kw)
        endTime = time.time()
        print('%s %s ms' % (fn.__name__, endTime - startime))
        return result
    return wrapper


@log
def now():
    print('2015-3-25')


now()


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print("测试成功!")