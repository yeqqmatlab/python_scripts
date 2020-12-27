from joblib import dump, load

clf = load('random_forest2.model')
print(clf)