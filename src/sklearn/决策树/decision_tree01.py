import matplotlib.pyplot as plt
import pandas as pd
from sklearn import tree
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定字体为楷体

# print(os.environ['PATH'])

# 准备数据
wine = load_wine()
# print(wine.data.shape)
# print(wine.target)

df = pd.concat([pd.DataFrame(wine.data), pd.DataFrame(wine.target)], axis=1)

# print(df)

# print(wine.feature_names)
# print(wine.target_names)

Xtrain, Xtest, Ytrain, Ytest = train_test_split(wine.data, wine.target, test_size=0.3)

# 选择模型

# clf = tree.DecisionTreeClassifier(criterion="entropy"
#                                   , random_state=30
#                                   , splitter="random"
#                                   , max_depth=3
#                                   # , min_samples_split=2
#                                   , min_samples_leaf=5
#                                   , min_impurity_decrease=0.2
#                                   )
# clf.fit(Xtrain, Ytrain)
#
#
# score = clf.score(Xtest, Ytest)
#
# print(score)
#
# score2 = clf.score(Xtrain, Ytrain)
# print(score2)
#
# # tree.plot_tree(clf)
#
#
# feature_name = ['酒精', '苹果酸', '灰', '灰的碱性', '镁', '总酚', '类黄酮', '非黄烷类酚类', '花青素', '颜色强度', '色调', 'od280/od315稀释葡萄酒', '脯氨酸']
#
# fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(12, 12), dpi=400)
#
# tree.plot_tree(clf,
#                feature_names=feature_name,
#                class_names=["琴酒", "雪莉", "贝尔摩德"],
#                filled=True)
# fig.savefig('image_name3.png')

# print(clf.feature_importances_)

# 特征 重要系数
# print([*zip(feature_name, clf.feature_importances_)])

scoreList = []
for i in range(10):
    clf = tree.DecisionTreeClassifier(max_depth=i + 1
                                      , criterion="entropy"
                                      , random_state=30
                                      , splitter="random"
                                      )
    clf = clf.fit(Xtrain, Ytrain)
    score3 = clf.score(Xtest, Ytest)
    scoreList.append(score3)

plt.plot(range(1, 11), scoreList, color="red", label="max_depth")
plt.legend()
plt.show()


# clf.apply(Xtest)
# print(clf.predict(Xtest))
