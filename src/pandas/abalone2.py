import pandas as pd
import warnings

warnings.filterwarnings('ignore')
abalone = pd.read_csv("abalone.csv")
abalone.head()

import matplotlib.pyplot as plt
import seaborn as sns

# 观察各个特征分布
i = 1  # 子图技术
plt.figure(figsize=(8, 4))
for col in abalone.columns[1:]:
    plt.subplot(4, 2, i)
    i = i + 1
    sns.distplot(abalone[col])
plt.tight_layout()

corr_df = abalone.corr()

fix, ax = plt.subplots(figsize=(12, 12))
# 绘制热力图
ax = sns.heatmap(corr_df, linewidths=.5,
                 cmap='Greens', annot=True, xticklabels=corr_df.columns,
                 yticklabels=corr_df.index)
ax.xaxis.set_label_position('top')
ax.xaxis.tick_top()

# 数据预处理
# 对sex进行onehot编码，便于后续模型纳入哑变量
sex_onehot = pd.get_dummies(abalone['sex'], prefix='sex')
abalone[sex_onehot.columns] = sex_onehot
abalone.head()

# 添加取值为1的特征
abalone['ones'] = 1
abalone.head()

# 根据鲍鱼环计算年龄
abalone['age'] = abalone['rings'] + 1.5
abalone.head()

y = abalone['age']
features_with_ones = ['length', 'diameter', 'height', 'whole_weight', 'shucked_weight', 'viscera_weight',
                      'shell_weight', 'sex_F', 'sex_M', 'ones']
features_without_ones = ['length', 'diameter', 'height', 'whole_weight', 'shucked_weight', 'viscera_weight',
                         'shell_weight', 'sex_F', 'sex_M']
x = abalone[features_with_ones]

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=111)

import numpy as np


# 能否算w ，需要判断是否可逆
def linear_regression(x, y):
    w = np.zeros_like(x.shape[1])
    if np.linalg.det(x.T.dot(x)) != 0:
        w = np.linalg.inv(x.T.dot(x)).dot(x.T).dot(y)
    return w


w = linear_regression(x, y)

w1 = pd.DataFrame(data=w, index=x.columns, columns=['numpy_w'])

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(x_train[features_without_ones], y_train)
print(lr.coef_)

w_lr = []
w_lr.extend(lr.coef_)
w_lr.append(lr.intercept_)
w1['lr_sklearn_w'] = w_lr
w1.round(decimals=2)

# def ridge_regression(x, y, ridge_lambda):
#     penalty_matrix = np.eye(x.shape[1])
#     penalty_matrix[x.shape[1] - 1][x.shape[1]] = 0
#     w = np.linalg.inv(x.T.dot(x) + ridge_lambda + penalty_matrix).dot(x.T).dot(y)
#     return w
#
#
# w2 = ridge_regression(x_train, y_train, 1.0)
# print(w2)

from sklearn.linear_model import Ridge

ridge = Ridge(alpha=1.0)
ridge.fit(x_train[features_without_ones], y_train)
w_ridge = []
w_ridge.extend(ridge.coef_)
w_ridge.append(ridge.intercept_)
w1['ridge_sklearn_w'] = w_ridge
w1.round(decimals=2)

alphas = np.logspace(-10, 10, 20)
coef = pd.DataFrame()
for alpha in alphas:
    ridge_clf = Ridge(alpha=alpha)
    ridge_clf.fit(x_train[features_without_ones], y_train)
    df = pd.DataFrame([ridge_clf.coef_], columns=x_train[features_without_ones].columns)
    df['alpha'] = alpha
    coef = coef.append(df, ignore_index=True)
coef.round(decimals=2)

alphas = np.logspace(-10, 10, 20)
coef = pd.DataFrame()
for alpha in alphas:
    ridge_clf = Ridge(alpha=alpha)
    ridge_clf.fit(x_train[features_without_ones], y_train)
    df = pd.DataFrame([ridge_clf.coef_], columns=x_train[features_without_ones].columns)
    df['alpha'] = alpha
    coef = coef.append(df, ignore_index=True)
coef.round(decimals=2)

import matplotlib.pyplot as plt

# 绘图
# 显示中文和正负号
plt.rcParams['font.sans-serif'] = ['SimHei', 'Time New Romam']
plt.rcParams['axes.unicode_minus'] = False

plt.rcParams['figure.dpi'] = 200
# 分辨率
plt.figure(figsize=(6, 3))
coef['alpha'] = coef['alpha']

for feature in x_train.columns[:-1]:
    plt.plot('alpha', feature, data=coef)
ax = plt.gca()
ax.set_xscale('log')
plt.legend(loc='upper right')
plt.xlabel(r'$\alpha$', fontsize=8)
plt.ylabel('系数', fontsize=8)

from sklearn.linear_model import Lasso

lasso = Lasso(alpha=0.01)
lasso.fit(x_train[features_without_ones], y_train)
print(lasso.coef_)
print(lasso.intercept_)

# lasso 的正则化路径
coef = pd.DataFrame()
for alpha in np.linspace(0.0001, 0.2, 20):
    lasso_clf = Lasso(alpha=alpha)
    lasso_clf.fit(x_train[features_without_ones], y_train)
    df = pd.DataFrame([lasso_clf.coef_], columns=x_train[features_without_ones].columns)
    df['alpha'] = alpha
    coef = coef.append(df, ignore_index=True)
coef.head()
# 绘图
plt.figure(figsize=(6, 3), dpi=200)
for feature in x_train.columns[:-1]:
    plt.plot('alpha', feature, data=coef)
plt.legend(loc='upper right')
plt.xlabel(r'$\alpha$', fontsize=5)
plt.ylabel('系数', fontsize=5)
# plt.show()

from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score

# mae
y_test_pred_lr = lr.predict(x_test.iloc[:, :-1])
print(round(mean_absolute_error(y_test, y_test_pred_lr), 4))

y_test_pred_ridge = ridge.predict(x_test[features_without_ones])
print(round(mean_absolute_error(y_test, y_test_pred_ridge), 4))

y_test_pred_lasso = lasso.predict(x_test[features_without_ones])
print(round(mean_absolute_error(y_test, y_test_pred_lasso), 4))

print("------------------------------->")
# mse
y_test_pred_lr = lr.predict(x_test.iloc[:, :-1])
print(round(mean_squared_error(y_test, y_test_pred_lr), 4))

y_test_pred_ridge = ridge.predict(x_test[features_without_ones])
print(round(mean_squared_error(y_test, y_test_pred_ridge), 4))

y_test_pred_lasso = lasso.predict(x_test[features_without_ones])
print(round(mean_squared_error(y_test, y_test_pred_lasso), 4))

print("r2系数------------------------------->")
# r2系数
print(round(r2_score(y_test, y_test_pred_lr), 4))
print(round(r2_score(y_test, y_test_pred_ridge), 4))
print(round(r2_score(y_test, y_test_pred_lasso), 4))

# 残差图
plt.figure(figsize=(6, 3), dpi=200)
y_train_pred_ridge = ridge.predict(x_train[features_without_ones])
plt.scatter(y_train_pred_ridge, y_train_pred_ridge - y_train, c='g', alpha=0.6)
plt.scatter(y_test_pred_ridge, y_test_pred_ridge - y_test, c='r', alpha=0.6)
plt.ylabel('Residuals')
plt.xlabel('Predict')
plt.show()
