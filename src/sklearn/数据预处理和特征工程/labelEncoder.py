from sklearn.preprocessing import LabelEncoder
import pandas as pd

data = pd.read_csv(r"E:\python_workspace\python_scripts\data\feature\Narrativedata.csv", index_col=0)

print(data.iloc[:, -1])

y = data.iloc[:, -1]

le = LabelEncoder()

label = le.fit_transform(y)

print(label)

data.iloc[:, -1] = label

print(data.head(100))

data.iloc[:, -1] = LabelEncoder().fit_transform(data.iloc[:, -1])









