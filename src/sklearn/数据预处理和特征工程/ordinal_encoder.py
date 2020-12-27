from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import OneHotEncoder
import pandas as pd


data = pd.read_csv(r"E:\python_workspace\python_scripts\data\feature\Narrativedata.csv", index_col=0)
data_ = data.copy()
data_.dropna(axis=0, inplace=True)


data_.iloc[:, 1: -1] = OrdinalEncoder().fit_transform(data_.iloc[:, 1: -1])


data2 = data.copy()

data2.dropna(axis=0, inplace=True)
x = data2.iloc[:, 1: -1]
print("---->", type(x))

enc = OneHotEncoder(categories='auto').fit(x)
enc = OneHotEncoder().fit(x)
tf = enc.transform(x)
res = tf.toarray()

print("-----------------------")
print(res)
print("-----------------------")

# res = OneHotEncoder(categories='auto').fit_transform(x).toarray()
print(res)
"""
[712 rows x 2 columns]
[[0. 1. 0. 0. 1.]
 [1. 0. 1. 0. 0.]
 [1. 0. 0. 0. 1.]
 ...
 [1. 0. 0. 0. 1.]
 [0. 1. 1. 0. 0.]
 [0. 1. 0. 1. 0.]]

"""

# 依然可以还原

print(enc.get_feature_names())  # ['x0_female' 'x0_male' 'x1_C' 'x1_Q' 'x1_S']

print(res.shape)  # (712, 5)

new_data = pd.concat([data, pd.DataFrame(res)], axis=1)

print(new_data.head())

new_data.drop(["Sex", "Embarked"], axis=1, inplace=True)

new_data.columns = ["Age", "Survived", "female", "male", "Embarked_C", "Embarked_Q", "Embarked_S"]

print(new_data.head())