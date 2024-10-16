import numpy as np
import matplotlib.pyplot as plt

# 定义Sigmoid函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 定义Logit函数
def logit(p):
    return np.log(p / (1 - p))

# 生成x值范围，适用于Sigmoid函数
x_vals = np.linspace(-10, 10, 400)

# 生成p值范围，适用于Logit函数（排除0和1）
p_vals = np.linspace(0.01, 0.99, 400)

# 计算Sigmoid和Logit函数的y值
sigmoid_vals = sigmoid(x_vals)
logit_vals = logit(p_vals)

# 创建图像
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# 绘制Sigmoid函数图像
ax[0].plot(x_vals, sigmoid_vals, color='blue', label='Sigmoid(x)')
ax[0].set_title('Sigmoid Function')
ax[0].set_xlabel('x')
ax[0].set_ylabel('Sigmoid(x)')
ax[0].grid(True)

# 绘制Logit函数图像
ax[1].plot(p_vals, logit_vals, color='red', label='Logit(p)')
ax[1].set_title('Logit Function')
ax[1].set_xlabel('p')
ax[1].set_ylabel('Logit(p)')
ax[1].grid(True)

# 显示图例
ax[0].legend()
ax[1].legend()

# 显示图像
plt.tight_layout()
plt.show()
