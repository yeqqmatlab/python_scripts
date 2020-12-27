import numpy as np
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

data = np.random.rand(100, 3)  # 生成一个随机数据，样本大小为100, 特征数为3


estimator = KMeans(n_clusters=3)  # 构造聚类器

y = estimator.fit_predict(data)  # 聚类

label_pred = estimator.labels_  # 获取聚类标签

centroids = estimator.cluster_centers_  # 获取聚类中心

print(label_pred)
print(centroids)

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(data[:, 0], data[:, 1], data[:, 2], c=y, marker='*')

ax.scatter(centroids[:, 0], centroids[:, 1], centroids[:, 2], marker='>')
plt.axis([0, 1, 0, 1])
plt.show()