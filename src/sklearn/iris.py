import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

red_x, red_y = [], []
blue_x, blue_y = [], []
green_x, green_y = [], []

#
data = load_iris()
x = data.data
y = data.target

pca = PCA(n_components=2)
reduce_x = pca.fit_transform(x)

for i in range(len(reduce_x)):
    if y[i] == 0:
        red_x.append(reduce_x[i][0])
        red_y.append(reduce_x[i][1])

    elif y[i] == 1:
        blue_x.append(reduce_x[i][0])
        blue_y.append(reduce_x[i][1])

    else:
        green_x.append(reduce_x[i][0])
        green_y.append(reduce_x[i][1])

# 可视化
plt.scatter(red_x, red_y, c='r', marker='x')
plt.scatter(blue_x, blue_y, c='b', marker='D')
plt.scatter(green_x, green_y, c='g', marker='.')
plt.show()

