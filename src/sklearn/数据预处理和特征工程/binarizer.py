import pandas as pd
from sklearn.preprocessing import Binarizer

data = pd.read_csv(r"E:\python_workspace\python_scripts\data\feature\Narrativedata.csv", index_col=0)

data.loc[:, "Age"] = data.loc[:, "Age"].fillna(data.loc[:, "Age"].median())

data2 = data.copy()

print(data2.iloc[:, 0])

X = data2.iloc[:, 0].values.reshape(-1, 1)

print(type(X))
print(X)
tf = Binarizer(threshold=30).fit_transform(X)

print(tf)
