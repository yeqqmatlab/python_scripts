from sklearn.preprocessing import MinMaxScaler
import pandas as pd

data = [[-1, 2], [-0.5, 6], [0, 10], [1, 18]]
df = pd.DataFrame(data)

# 实现归一化
scaler = MinMaxScaler()

# scaler = scaler.fit(df)
# res = scaler.transform(df)

res = scaler.fit_transform(df)

print(scaler.inverse_transform(res))


# print(res)

# print(df.info())
