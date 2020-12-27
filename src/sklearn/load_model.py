from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn import datasets
import joblib

iris = datasets.load_iris()

iris_x = iris.data
iris_y = iris.target
# 利用train_test_split进行将训练集和测试集进行分开，test_size占30%
X_train, X_test, y_train, y_test = train_test_split(iris_x, iris_y, test_size=0.3)


model = joblib.load('/src/model/iris_model.pkl')
print(y_test)
print(model.predict(X_test[:]))