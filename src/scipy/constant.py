import scipy.constants as C
from scipy import integrate

print(C.pi)
print(C.g)
print(C.G)

y = lambda x: x ** 2 + 3

res, d = integrate.quad(y, -2, 4)
print(res, d)
