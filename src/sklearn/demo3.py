
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier   # 利用邻近点方式训练数据集

#### 引入数据集 ####

iris = datasets.load_iris()

iris_x = iris.data
iris_y = iris.target

# 利用train_test_split进行将训练集和测试集进行分开，test_size占30%
X_train, X_test, y_train, y_test = train_test_split(iris_x, iris_y, test_size=0.3)

# 我们看到训练数据的特征值分为3类
print(y_train)

# 训练数据
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)

# 预测数据
print(knn.predict(X_test))

print(y_test)

















