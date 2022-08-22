import matplotlib.pyplot as plt

# plt.scatter(2, 4)
# plt.scatter(3, 4)
# plt.scatter(4, 4)
# plt.scatter(4, 4, s=200)
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

x_values = list(range(1, 100))
y_values = [x ** 2 for x in x_values]
plt.scatter(x_values, y_values, s=40, edgecolors='none')
plt.axes([0, 50, 0, 1000])
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.show()


