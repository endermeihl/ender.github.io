# 导入所需库
import numpy as np
import matplotlib.pyplot as plt

# 定义逻辑代价函数的两个部分
def cost_1(h):
    return -np.log(h)

def cost_0(h):
    return -np.log(1 - h)

# 生成 h 值的范围 (避免 0 和 1)
h_vals = np.linspace(0.01, 0.99, 100)

# 计算代价函数
cost_when_y_is_1 = cost_1(h_vals)
cost_when_y_is_0 = cost_0(h_vals)

# 绘制逻辑代价函数的图像
plt.figure(figsize=(8, 6))
plt.plot(h_vals, cost_when_y_is_1, label='$Cost(h_\\theta(x), y=1)$', color='red')
plt.plot(h_vals, cost_when_y_is_0, label='$Cost(h_\\theta(x), y=0)$', color='blue')
plt.title('Logistic Cost Function', fontsize=16)
plt.xlabel('$h_\\theta(x)$ (Prediction)', fontsize=12)
plt.ylabel('Cost', fontsize=12)
plt.grid(True)
plt.legend()
plt.show()
