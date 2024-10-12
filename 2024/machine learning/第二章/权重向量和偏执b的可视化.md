为了将感知器模型中的权重向量 w_可视化，我们可以在原有的点阵图上绘制最终的分类边界，同时显示权重向量 w_。权重向量 w_是决策边界的法向量，因此它垂直于分类边界。在二维情况下，我们可以通过显示这个向量来更直观地理解模型的决策过程。

### 扩展代码以可视化权重向量 w_：

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# 感知器类的实现
class Perceptron(object):
    def __init__(self, eta=0.01, n_iter=50, random_state=1):
        self.eta = eta  # 学习率
        self.n_iter = n_iter  # 迭代次数
        self.random_state = random_state  # 随机种子，用于生成初始权重

    def fit(self, X, y):
        # 使用给定的随机种子生成正态分布的初始权重，权重的数量是1 + 特征数量
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])
        self.errors_ = []

        # 开始进行训练迭代
        for _ in range(self.n_iter):
            errors = 0  # 记录本轮的误分类次数
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi  # 更新权重
                self.w_[0] += update  # 更新偏置
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    def net_input(self, X):
        """计算净输入"""
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        """根据净输入返回分类标签"""
        return np.where(self.net_input(X) >= 0.0, 1, -1)

# 读取 Iris 数据集
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
y = df.iloc[0:100, 4].values  # 获取前100个样本的标签
y = np.where(y == 'Iris-setosa', -1, 1)  # 将标签转化为 -1 和 1
X = df.iloc[0:100, [0, 2]].values  # 获取前100个样本的特征（花萼和花瓣长度）

# 训练感知器模型
ppn = Perceptron(eta=0.1, n_iter=10)
ppn.fit(X, y)

# 绘制点阵图和决策边界
def plot_decision_regions(X, y, classifier, resolution=0.02):
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    # 绘制决策区域
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    # 绘制分类点
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], 
                    y=X[y == cl, 1],
                    alpha=0.8, 
                    c=colors[idx],
                    marker=markers[idx], 
                    label=cl, 
                    edgecolor='black')

# 绘制决策边界和点阵图
plot_decision_regions(X, y, classifier=ppn)
plt.xlabel('sepal length [cm]')
plt.ylabel('petal length [cm]')
plt.legend(loc='upper left')

# 绘制最终的权重向量 w_ 以及其对应的决策边界
w = ppn.w_[1:]  # 获取权重向量
b = ppn.w_[0]  # 获取偏置
x1_vals = np.linspace(X[:, 0].min() - 1, X[:, 0].max() + 1, 100)

# 计算直线的斜率和截距: -w[0] / w[1] 是决策边界的斜率，-b / w[1] 是截距
decision_boundary = -(w[0] / w[1]) * x1_vals - b / w[1]
plt.plot(x1_vals, decision_boundary, 'k--', label='decision boundary')

# 绘制权重向量 w_ (法向量) 从 (0, 0) 开始，长度和 w 成比例
origin = np.array([X[:, 0].mean(), X[:, 1].mean()])  # 从数据中心绘制向量
plt.quiver(origin[0], origin[1], w[0], w[1], angles='xy', scale_units='xy', scale=1, color='green', label='weight vector w_')

plt.legend(loc='upper left')
plt.show()
```

### 代码解释：
1. **训练感知器模型**：
   - 使用感知器模型训练 Iris 数据集中的前 100 个样本，得到分类的权重向量 w_和偏置 \( b \)。

2. **绘制点阵图和决策区域**：
   - `plot_decision_regions()` 函数绘制数据点和感知器模型的决策区域，将两个类别的样本点以不同颜色显示。
   
3. **绘制决策边界**：
   - 使用感知器学习到的权重向量 w_和偏置 \( b \) 计算决策边界的直线方程：
     \[
     x_2 = -\frac{w_1}{w_2} x_1 - \frac{b}{w_2}
     \]
   - 该直线通过数据点的特征空间划分不同的类别。

4. **绘制权重向量 w_**：
   - 使用 `plt.quiver()` 函数从数据的中心位置绘制出权重向量 w_，它是决策边界的法向量。
   - 权重向量的方向决定了决策边界的方向，而偏置 \( b \) 控制决策边界在特征空间中的位置。

### 可视化结果：
- 决策边界是一条虚线，表示分类的边界。
- 绿色的箭头代表权重向量 w_，它与决策边界垂直，方向决定了分类边界的方向。
