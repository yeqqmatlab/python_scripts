
from sklearn import datasets
from sklearn.linear_model import LinearRegression  # 引入线性回归模型

# 导入数据

load_data = datasets.load_boston()

data_X = load_data.data
data_y = load_data.target

print(data_X.shape)
# (506,13) data_X共13个特征变量

model = LinearRegression()
model.fit(data_X, data_y)
model.predict(data_X[:4, :])

print(model.coef_)

print(model.intercept_)

print(model.get_params())

print(model.score(data_X, data_y))


















