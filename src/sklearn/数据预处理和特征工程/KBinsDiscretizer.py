import pandas as pd
from sklearn.preprocessing import KBinsDiscretizer

data = pd.read_csv(r"E:\python_workspace\python_scripts\data\feature\Narrativedata.csv", index_col=0)
data.loc[:, "Age"] = data.loc[:, "Age"].fillna(data.loc[:, "Age"].median())
data2 = data.copy()
data2.iloc[:, 0].fillna(0)
print(data2.iloc[:, 0])

X = data2.iloc[:, 0].values.reshape(-1, 1)

est = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='uniform')
res = est.fit_transform(X)
print(res)

est2 = KBinsDiscretizer(n_bins=3, encode='onehot', strategy='uniform')
print(est2.fit_transform(X).toarray())
