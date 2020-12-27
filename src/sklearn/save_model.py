from sklearn import svm
from sklearn import datasets
import joblib

iris = datasets.load_iris()
X, y = iris.data, iris.target
model = svm.SVC()
model.fit(X, y)

# 引入sklearn中自带的保存模块
joblib.dump(model, '/src/model/iris_model.pkl')

