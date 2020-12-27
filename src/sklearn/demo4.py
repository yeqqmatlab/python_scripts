
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier   # 利用邻近点方式训练数据集
import matplotlib.pyplot as plt

#### 引入数据集 ####

X, y = datasets.make_regression(n_samples=100, n_features=1, n_targets=1, noise=1)

### 绘制构造的数据 ###

plt.figure()
plt.scatter(X, y)
plt.show()

















