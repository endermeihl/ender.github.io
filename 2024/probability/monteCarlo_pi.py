import numpy as np

# 定义模拟的次数，即抽样的数量
N = 1000000

# 在单位正方形中随机生成点
x = np.random.uniform(0, 1, N)
y = np.random.uniform(0, 1, N)

# 计算这些点到原点的距离，然后判断这些点是否在单位圆内
distances = np.sqrt(x**2 + y**2)
in_circle = distances <= 1

# 计算落在单位圆内的点的数量
num_in_circle = np.sum(in_circle)

# 估计圆周率的值
pi_estimate = 4 * num_in_circle / N

print("Estimate of pi:", pi_estimate)