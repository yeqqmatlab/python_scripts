# 数值积分
# 无直接原函数
from scipy import integrate
import numpy as np

Y = lambda x: x ** 2 + 3

x = np.linspace(-2, 4, 10)
y = Y(x)
print(x)
print(y)

res = integrate.trapz(y, x)
print(res)
