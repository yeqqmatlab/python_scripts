import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("/Users/yqq/PycharmProjects/python_scripts/data/train.csv")
# print(df.head())
print(df.info())
print(df.size)

df.drop(["Name", "Cabin", "Ticket"], inplace=True, axis=1)

print(df.info())

df["Age"] = df["Age"].fillna(df["Age"].mean())

print(df.info())

df = df.dropna()

print(df.info())

labels = df["Embarked"].unique().tolist()

df["Embarked"] = df["Embarked"].apply(lambda x: labels.index(x))

print(df)

df["Sex"] = (df["Sex"] == "male").astype("int")

print(df)

X = df.iloc[:, df.columns != "Survived"]

print(X)

Y = df.iloc[:, df.columns == "Survived"]

print(Y)

Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y, test_size=0.3, random_state=10)

# print(Xtrain)
#
# for i in [Xtrain, Xtest, Ytrain, Ytest]:
#     i.index = range(i.shape[0])
#
# print(Xtrain)
#
# clf = DecisionTreeClassifier(random_state=25
#                              , max_depth=3
#                              )
#
# clf.fit(Xtrain, Ytrain)
#
# score = clf.score(Xtest, Ytest)
#
# # clf2 = DecisionTreeClassifier(random_state=25)
#
# print(score)

print("----------------->")

# cross_score = cross_val_score(clf, X, Y, cv=10).mean()
# print("-->", cross_score)

# train = []
# test = []
# for i in range(10):
#     clf = DecisionTreeClassifier(random_state=25
#                                  , max_depth=i + 1
#                                  )
#
#     clf = clf.fit(Xtrain, Ytrain)
#     score_train = clf.score(Xtrain, Ytrain)
#     score_test = cross_val_score(clf, X, Y, cv=10).mean()
#     train.append(score_train)
#     test.append(score_test)
#
# # print(max(test))
# plt.plot(range(1, 11), train, color="black", label="train")
# plt.plot(range(1, 11), test, color="blue", label="test")
# plt.xticks(range(1, 11))
# plt.legend()
# plt.show()

# 网格搜索
# 一串参数和这些参数对应的取值范围

gini_threholds = np.linspace(0, 0.5, 20)

parameter = {"criterion": ("gini", "entropy")
    , "splitter": ("best", "random")
    , "max_depth": [*range(1, 6)]
    , "min_samples_leaf": [*range(1, 50, 5)]
    , "min_impurity_decrease": gini_threholds}

clf_gs = DecisionTreeClassifier(random_state=25)
GS = GridSearchCV(clf_gs, parameter, cv=10)
GS.fit(Xtrain, Ytrain)

print("best_params_  --->", GS.best_params_)
print("best_score_  --->", GS.best_score_)



# best_params_  ---> {'criterion': 'entropy', 'max_depth': 4, 'min_impurity_decrease': 0.0, 'min_samples_leaf': 1, 'splitter': 'best'}
# best_score_  ---> 0.8215309779825908
