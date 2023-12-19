import numpy as np

# 定义函数
def f(x):
    return x**2

# 定义积分的区间
a = 0
b = 1

# 定义模拟的次数，即抽样的数量
N = 100000

# 生成 [a, b] 区间内的随机数
x = np.random.uniform(a, b, N)
print(x.shape)

# 计算函数在这些点上的值
y = f(x)

# 计算积分的估计值
integral = (b - a) * np.sum(y) / N

print("Integral:", integral)