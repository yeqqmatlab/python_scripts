import pandas as pd
import warnings
import matplotlib.pyplot as plt
import seaborn as sns

warnings.filterwarnings('ignore')

abalone = pd.read_csv("abalone.csv")
print(abalone.head())
print(abalone.describe())
print(abalone.sex.value_counts())

i = 1
plt.figure(figsize=(16, 8))
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
print(abalone.head())

# 添加取值为1的特征
abalone['ones'] = 1
abalone.head()

# 根据鲍鱼环计算年龄
abalone['age'] = abalone['rings'] + 1.5
print(abalone.head())

y = abalone['age']
features_with_ones = ['length', 'diameter', 'height', 'whole_weight', 'shucked_weight', 'viscera_weight',
                      'shell_weight', 'sex_F', 'sex_M', 'ones']
features_without_ones = ['length', 'diameter', 'height', 'whole_weight', 'shucked_weight', 'viscera_weight',
                         'shell_weight', 'sex_F', 'sex_M']
x = abalone[features_with_ones]
print(x)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=111)

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(x_train[features_without_ones], y_train)
print(lr.coef_)


from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
#mae
y_test_pred_lr = lr.predict(x_test.iloc[:, :-1])
print("mae---->")
print(round(mean_absolute_error(y_test, y_test_pred_lr), 4))

# mse
y_test_pred_lr = lr.predict(x_test.iloc[:, :-1])
print("mse---->")
print(round(mean_squared_error(y_test, y_test_pred_lr), 4))

#r2系数
print("r2---->")
print(round(r2_score(y_test,y_test_pred_lr),4))


from sklearn.linear_model import Ridge
ridge=Ridge(alpha=1.0)
ridge.fit(x_train[features_without_ones],y_train)
w_ridge=[]
w_ridge.extend(ridge.coef_)
w_ridge.append(ridge.intercept_)

print(w_ridge)



from sklearn.linear_model import Ridge
ridge=Ridge(alpha=1.0)
ridge.fit(x_train[features_without_ones],y_train)
w_ridge=[]
w_ridge.extend(ridge.coef_)
w_ridge.append(ridge.intercept_)






