import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y, linewidth=2)
plt.title("Square", fontsize=24)
plt.xlabel("number", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# plt.title()
# plt.xlabel()
# plt.ylabel()
plt.show()
