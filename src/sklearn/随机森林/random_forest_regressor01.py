from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import train_test_split
from scipy.stats import randint
from joblib import dump, load

X, y = fetch_california_housing(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# define the parameter space that will be searched over
param_distributions = {'n_estimators': randint(1, 30)
    , 'max_depth': randint(3, 10)}

search = RandomizedSearchCV(estimator=RandomForestRegressor(random_state=0), n_iter=5,
                            param_distributions=param_distributions, random_state=0)

search.fit(X_train, y_train)

print(search.best_params_)

score = search.score(X_test, y_test)
print(score)

# 模型持久化
dump(search, 'random_forest2.model')
