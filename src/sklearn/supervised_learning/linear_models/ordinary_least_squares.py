print(__doc__)

"""
线性回归知识及预测糖尿病实例
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


# Load the diabetes dataset
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

print(type(diabetes_X))
# <class 'numpy.ndarray'>
print(diabetes_X.shape)
# (442, 10)

diabetes_dataFrame = datasets.load_diabetes()
diabetes_X_train, diabetes_X_test, diabetes_y_train, diabetes_y_test = train_test_split(diabetes_dataFrame.data[:, np.newaxis, 2],
                                                                                        diabetes_dataFrame.target,
                                                                                        test_size=0.3)




# # Use only one feature
# diabetes_X = diabetes_X[:, np.newaxis, 2]
# print(diabetes_X.shape)
# # (442, 1)
#
# # Split the data into training/testing sets
# diabetes_X_train = diabetes_X[:-20]
# diabetes_X_test = diabetes_X[-20:]
#
# # Split the targets into training/testing sets
# diabetes_y_train = diabetes_y[:-20]
# diabetes_y_test = diabetes_y[-20:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)

print("coef---->", regr.coef_)
print("intercept---->", regr.intercept_)

# 回归用score不合适
# score = regr.score(diabetes_X_test, diabetes_y_test)
#
# print("score--->", score)

# Make predictions using the testing set
diabetes_y_pred = regr.predict(diabetes_X_test)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print('Mean squared error: %.2f'
      % mean_squared_error(diabetes_y_test, diabetes_y_pred))
# The coefficient of determination: 1 is perfect prediction
print('Coefficient of determination: %.2f'
      % r2_score(diabetes_y_test, diabetes_y_pred))

# Plot outputs
plt.scatter(diabetes_X_test, diabetes_y_test,  color='black')
plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()