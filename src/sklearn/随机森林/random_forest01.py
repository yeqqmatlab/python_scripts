# from sklearn.ensemble import RandomForestClassifier
#
# X = [[0, 0], [1, 1]]
#
# Y = [0, 1]
#
# clf = RandomForestClassifier(n_estimators=10)
#
# clf.fit(X, Y)

# print(clf.feature_importances_)

from sklearn.ensemble import RandomForestClassifier
X = [[0,0], [1,1]]
Y = [0,1]
clf = RandomForestClassifier(n_estimators=10)
clf.fit(X,Y)


