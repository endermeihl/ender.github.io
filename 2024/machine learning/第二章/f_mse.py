import numpy as np
import matplotlib.pyplot as plt

# 定义损失函数（简单的二次函数表示抛物面）
def cost_function(theta_0, theta_1):
    return theta_0**2 + theta_1**2

# 定义梯度函数
def gradient(theta_0, theta_1):
    return 2 * theta_0, 2 * theta_1

# 设置学习率和初始值
learning_rate = 0.1
theta_0, theta_1 = 3, 3  # 初始参数
iterations = 20

# 记录参数更新的路径
theta_0_vals = [theta_0]
theta_1_vals = [theta_1]

# 执行梯度下降
for _ in range(iterations):
    grad_0, grad_1 = gradient(theta_0, theta_1)
    theta_0 -= learning_rate * grad_0
    theta_1 -= learning_rate * grad_1
    theta_0_vals.append(theta_0)
    theta_1_vals.append(theta_1)

# 绘制等高线图
theta_0_range = np.linspace(-4, 4, 100)
theta_1_range = np.linspace(-4, 4, 100)
theta_0_grid, theta_1_grid = np.meshgrid(theta_0_range, theta_1_range)
cost_vals = cost_function(theta_0_grid, theta_1_grid)

plt.contour(theta_0_grid, theta_1_grid, cost_vals, levels=20)
plt.plot(theta_0_vals, theta_1_vals, 'ro-', label='Gradient Descent Path')
plt.title('Gradient Descent Path on Contour Plot')
plt.xlabel(r'$\theta_0$')
plt.ylabel(r'$\theta_1$')
plt.legend()
plt.show()
