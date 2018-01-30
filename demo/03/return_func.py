# -*- coding: utf-8 -*-


def count():
    fs = []
    for i in range(1, 4):

        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())


def count2():
    def f(j):
        return lambda: j * j

    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f1, f2, f3 = count2()

print(f1())
print(f2())
print(f3())


def createCounter():
    f = [0]
    def counter():
        f[0] = f[0] + 1
        return f[0]

    return counter

# 测试

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')