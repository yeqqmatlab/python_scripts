import pandas as pd

data = pd.read_csv(r"E:\python_workspace\python_scripts\data\feature\Narrativedata.csv", index_col=0)

print(data.head())
print(data.info())

data.loc[:, "Age"] = data.loc[:, "Age"].fillna(data.loc[:, "Age"].median())

print(data.info())

print(data.loc[:, "Age"])