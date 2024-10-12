# 导入必要的库
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# 感知器类的实现
class Perceptron(object):
    """
    感知器分类器的实现

    Parameters
    ------------
    eta : float
        学习率 (0.0 到 1.0 之间的值)
    n_iter : int
        数据集的迭代次数（即训练的epoch数）。
    random_state : int
        随机数生成器的种子，用于初始化权重。

    Attributes
    -----------
    w_ : 1d-array
        训练后的权重。
    errors_ : list
        每个epoch中的误分类次数（更新次数）。
    """
    
    # 初始化感知器的参数
    def __init__(self, eta=0.01, n_iter=50, random_state=1):
        self.eta = eta  # 学习率
        self.n_iter = n_iter  # 迭代次数
        self.random_state = random_state  # 随机种子，用于生成初始权重

    def fit(self, X, y):
        """
        训练感知器模型，根据训练数据调整权重。

        Parameters
        ----------
        X : {array-like}, shape = [n_examples, n_features]
            训练向量（特征矩阵），其中 n_examples 是样本数量，n_features 是特征数量。
        y : array-like, shape = [n_examples]
            目标值（分类标签）。

        Returns
        -------
        self : object
        """
        # 使用给定的随机种子生成正态分布的初始权重，权重的数量是1 + 特征数量
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])
        
        # 初始化用于记录每轮误分类错误次数的列表
        self.errors_ = []

        # 开始进行训练迭代
        for _ in range(self.n_iter):
            errors = 0  # 记录本轮的误分类次数
            # 遍历训练集中每一个样本 (xi) 和对应的目标标签 (target)
            for xi, target in zip(X, y):
                # 计算更新值（学习率 * (真实值 - 预测值)）
                update = self.eta * (target - self.predict(xi))
                # 更新权重，权重更新公式：w = w + η * Δw
                self.w_[1:] += update * xi
                # 更新偏置，偏置的权重相当于 w_ 的第一个元素
                self.w_[0] += update
                # 记录本次是否有误分类（update != 0 表示有更新，意味着预测错误）
                errors += int(update != 0.0)
            # 记录每轮的误分类次数
            self.errors_.append(errors)
        return self

    def net_input(self, X):
        """计算净输入：特征和权重的加权和加上偏置"""
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        """根据净输入返回分类标签，使用单位阶跃函数进行预测"""
        return np.where(self.net_input(X) >= 0.0, 1, -1)


# 示例：使用感知器类和 numpy 操作
v1 = np.array([1, 2, 3])  # 创建向量 v1
v2 = 0.5 * v1  # 创建向量 v2 是 v1 的一半
# 计算 v1 和 v2 的夹角
np.arccos(v1.dot(v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))


# 读取 Iris 数据集
s = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
print('URL:', s)

df = pd.read_csv(s, header=None, encoding='utf-8')  # 通过 URL 加载数据
df.tail()  # 查看数据集的后几行

# 选择 'Iris-setosa' 和 'Iris-versicolor' 两类数据
y = df.iloc[0:100, 4].values  # 获取前100个样本的标签（第5列）
y = np.where(y == 'Iris-setosa', -1, 1)  # 将标签转化为 -1 和 1

# 提取花萼长度和花瓣长度作为特征
X = df.iloc[0:100, [0, 2]].values  # 获取前100个样本的特征（花萼和花瓣长度）

# 可视化数据：绘制两个类别的散点图
plt.scatter(X[:50, 0], X[:50, 1], color='red', marker='o', label='setosa')
plt.scatter(X[50:100, 0], X[50:100, 1], color='blue', marker='x', label='versicolor')

plt.xlabel('sepal length [cm]')  # X轴标签
plt.ylabel('petal length [cm]')  # Y轴标签
plt.legend(loc='upper left')  # 图例位置

plt.show()  # 显示图像

# 训练感知器模型
ppn = Perceptron(eta=0.1, n_iter=10)  # 初始化感知器
ppn.fit(X, y)  # 使用特征 X 和标签 y 训练感知器模型

# 绘制每个 epoch 的误分类次数
plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
plt.xlabel('Epochs')  # X轴标签
plt.ylabel('Number of updates')  # Y轴标签
plt.show()  # 显示图像

# 绘制决策区域的函数
def plot_decision_regions(X, y, classifier, resolution=0.02):
    # 生成用于绘制决策区域的颜色和标记
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

# 调用函数，绘制感知器模型的决策区域
plot_decision_regions(X, y, classifier=ppn)
plt.xlabel('sepal length [cm]')  # X轴标签
plt.ylabel('petal length [cm]')  # Y轴标签
plt.legend(loc='upper left')  # 图例位置
plt.show()  # 显示图像

# 自适应线性神经元(Adaline)类的实现
class AdalineGD(object):
    """
    自适应线性神经元分类器，使用梯度下降进行优化。

    Parameters
    ------------
    eta : float
        学习率 (0.0 到 1.0 之间的值)
    n_iter : int
        数据集的迭代次数（即训练的epoch数）。
    random_state : int
        随机数生成器的种子，用于初始化权重。

    Attributes
    -----------
    w_ : 1d-array
        训练后的权重。
    cost_ : list
        每个epoch的成本函数值（误差平方和）。
    """
    
    # 初始化 Adaline 的参数
    def __init__(self, eta=0.01, n_iter=50, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, X, y):
        """
        训练 Adaline 模型。

        Parameters
        ----------
        X : {array-like}, shape = [n_examples, n_features]
            训练向量（特征矩阵），其中 n_examples 是样本数量，n_features 是特征数量。
        y : array-like, shape = [n_examples]
            目标值（分类标签）。

        Returns
        -------
        self : object
        """
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])
        self.cost_ = []

        for i in range(self.n_iter):
            net_input = self.net_input(X)
            output = self.activation(net_input)
            errors = (y - output)
            self.w_[1:] += self.eta * X.T.dot(errors)
            self.w_[0] += self.eta * errors.sum()
            cost = (errors**2).sum() / 2.0
            self.cost_.append(cost)
        return self

    def net_input(self, X):
        """计算净输入：特征和权重的加权和加上偏置"""
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def activation(self, X):
        """线性激活函数"""
        return X

    def predict(self, X):
        """根据净输入返回分类标签"""
        return np.where(self.activation(self.net_input(X)) >= 0.0, 1, -1)

# 创建和训练 Adaline 模型并绘制结果
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))

ada1 = AdalineGD(n_iter=10, eta=0.01).fit(X, y)
ax[0].plot(range(1, len(ada1.cost_) + 1), np.log10(ada1.cost_), marker='o')
ax[0].set_xlabel('Epochs')
ax[0].set_ylabel('log(Sum-squared-error)')
ax[0].set_title('Adaline - Learning rate 0.01')

ada2 = AdalineGD(n_iter=10, eta=0.0001).fit(X, y)
ax[1].plot(range(1, len(ada2.cost_) + 1), ada2.cost_, marker='o')
ax[1].set_xlabel('Epochs')
ax[1].set_ylabel('Sum-squared-error')
ax[1].set_title('Adaline - Learning rate 0.0001')

plt.show()

# 特征标准化：标准化特征值以提高梯度下降的收敛速度
X_std = np.copy(X)
X_std[:, 0] = (X[:, 0] - X[:, 0].mean()) / X[:, 0].std()
X_std[:, 1] = (X[:, 1] - X[:, 1].mean()) / X[:, 1].std()

# 使用标准化数据训练 Adaline 模型
ada_gd = AdalineGD(n_iter=15, eta=0.01)
ada_gd.fit(X_std, y)

# 绘制决策边界
plot_decision_regions(X_std, y, classifier=ada_gd)
plt.title('Adaline - Gradient Descent')
plt.xlabel('sepal length [standardized]')
plt.ylabel('petal length [standardized]')
plt.legend(loc='upper left')
plt.show()

# 绘制误差平方和
plt.plot(range(1, len(ada_gd.cost_) + 1), ada_gd.cost_, marker='o')
plt.xlabel('Epochs')
plt.ylabel('Sum-squared-error')
plt.show()

# 随机梯度下降的 Adaline 实现
class AdalineSGD(object):
    """
    自适应线性神经元分类器，使用随机梯度下降优化。

    Parameters
    ------------
    eta : float
        学习率 (0.0 到 1.0 之间的值)
    n_iter : int
        数据集的迭代次数（即训练的epoch数）。
    shuffle : bool (default: True)
        每个epoch是否打乱数据，防止循环。
    random_state : int
        随机数生成器的种子，用于初始化权重。

    Attributes
    -----------
    w_ : 1d-array
        训练后的权重。
    cost_ : list
        每个epoch的平均成本函数值。
    """
    
    # 初始化 AdalineSGD 的参数
    def __init__(self, eta=0.01, n_iter=10, shuffle=True, random_state=None):
        self.eta = eta
        self.n_iter = n_iter
        self.shuffle = shuffle
        self.random_state = random_state
        self.w_initialized = False

    def fit(self, X, y):
        """
        训练 AdalineSGD 模型。

        Parameters
        ----------
        X : {array-like}, shape = [n_examples, n_features]
            训练向量（特征矩阵），其中 n_examples 是样本数量，n_features 是特征数量。
        y : array-like, shape = [n_examples]
            目标值（分类标签）。

        Returns
        -------
        self : object
        """
        self._initialize_weights(X.shape[1])
        self.cost_ = []

        for i in range(self.n_iter):
            if self.shuffle:
                X, y = self._shuffle(X, y)
            cost = []
            for xi, target in zip(X, y):
                cost.append(self._update_weights(xi, target))
            avg_cost = sum(cost) / len(y)
            self.cost_.append(avg_cost)
        return self

    def partial_fit(self, X, y):
        """对训练数据进行增量训练，不重新初始化权重"""
        if not self.w_initialized:
            self._initialize_weights(X.shape[1])
        if y.ravel().shape[0] > 1:
            for xi, target in zip(X, y):
                self._update_weights(xi, target)
        else:
            self._update_weights(X, y)
        return self

    def _shuffle(self, X, y):
        """随机打乱训练数据"""
        r = self.rgen.permutation(len(y))
        return X[r], y[r]

    def _initialize_weights(self, m):
        """初始化权重为较小的随机数"""
        self.rgen = np.random.RandomState(self.random_state)
        self.w_ = self.rgen.normal(loc=0.0, scale=0.01, size=1 + m)
        self.w_initialized = True

    def _update_weights(self, xi, target):
        """应用 Adaline 学习规则更新权重"""
        output = self.activation(self.net_input(xi))
        error = (target - output)
        self.w_[1:] += self.eta * xi.dot(error)
        self.w_[0] += self.eta * error
        cost = 0.5 * error**2
        return cost

    def net_input(self, X):
        """计算净输入：特征和权重的加权和加上偏置"""
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def activation(self, X):
        """线性激活函数"""
        return X

    def predict(self, X):
        """根据净输入返回分类标签"""
        return np.where(self.activation(self.net_input(X)) >= 0.0, 1, -1)

# 创建和训练 AdalineSGD 模型并绘制结果
ada_sgd = AdalineSGD(n_iter=15, eta=0.01, random_state=1)
ada_sgd.fit(X_std, y)

plot_decision_regions(X_std, y, classifier=ada_sgd)
plt.title('Adaline - Stochastic Gradient Descent')
plt.xlabel('sepal length [standardized]')
plt.ylabel('petal length [standardized]')
plt.legend(loc='upper left')
plt.show()

# 绘制平均成本函数值
plt.plot(range(1, len(ada_sgd.cost_) + 1), ada_sgd.cost_, marker='o')
plt.xlabel('Epochs')
plt.ylabel('Average Cost')
plt.show()

# 增量更新模型权重
ada_sgd.partial_fit(X_std[0, :], y[0])
