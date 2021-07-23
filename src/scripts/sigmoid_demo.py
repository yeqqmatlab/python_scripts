import numpy
import math
import matplotlib.pyplot as plt

"""
逻辑回归 函数
"""

def sigmoid(x):
    a = []
    for item in x:
        a.append(1.0 / (1.0 + math.exp(-item)))
    return a


x = numpy.arange(-10, 10, 1)
y = sigmoid(x)
# print(y)
# arr = [1,2,3,4,5]
# print(sigmoid(arr))
plt.plot(x, y)
plt.show()

print(help(numpy.arange))