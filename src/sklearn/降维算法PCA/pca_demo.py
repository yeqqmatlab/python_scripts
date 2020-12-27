from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import pandas as pd

# 准备数据集
iris = load_iris()
y = iris.target
X = iris.data

print(y)
print(y.shape)
# print(X)
# print(X.shape)

X_DF = pd.DataFrame(X)

print(X_DF)

# 建模
pca = PCA(n_components=2)  # 实例化
X_dr = pca.fit_transform(X_DF)  # 训练模型

# print(X_dr)

# 可视化
# print(y == 0)
# print(X_dr[:, 0])
# bool索引
# print(X_dr[y == 0, 0].shape)


colors = ['red','black','orange']
plt.Figure()
for i in [0, 1, 2]:
    plt.scatter(X_dr[y == i, 0]
                , X_dr[y == i, 1]
                , alpha= 0.7
                , c=colors[i]
                , label=iris.target_names[i]
                )

plt.legend()
plt.title('PCA of IRIS data sets')
plt.show()





