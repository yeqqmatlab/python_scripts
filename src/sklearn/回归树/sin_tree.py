import numpy as np
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt

# create random dataset

rng = np.random.RandomState(1)
X = np.sort(5 * rng.rand(80, 1), axis=0)

# 降维
y = np.sin(X).ravel()
# 添加噪声
y[::5] += 3 * (0.5 - rng.random(16))

tree2 = DecisionTreeRegressor(max_depth=2)
tree5 = DecisionTreeRegressor(max_depth=5)

# fit regression tree
tree2.fit(X, y)
tree5.fit(X, y)

# predict
X_test = np.arange(0, 5, 0.01)[:, np.newaxis]
y2 = tree2.predict(X_test)
y5 = tree5.predict(X_test)

# plot the res

plt.figure()
plt.scatter(X, y, s=20
            , edgecolors="black"
            , c="darkorange"
            , label="data")

plt.plot(X_test, y2, color="cornflowerblue",
         label="max_depth=2", linewidth=2)
plt.plot(X_test, y5, color="yellowgreen", label="max_depth=5", linewidth=2)
plt.xlabel("data")
plt.ylabel("target")
plt.title("Decision Tree Regression")
plt.legend()
plt.show()
