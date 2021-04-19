import tensorflow as tf
from matplotlib import pyplot as plt

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 可视化训练集输入特征的第一个元素
plt.imshow(x_train[1], cmap='gray')
plt.show()

# 打印出训练集输入特征的第一个元素
print("x_train[0]:\n", x_train[1])
# 打印出训练集标签的第一个元素
print("y_train[0]:\n", y_train[1])

# 打印出整个训练集输入特征形状 6 万张照片 28*28矩阵
print("x_train.shape:\n", x_train.shape)
# 打印出整个训练集标签的形状
print("y_train.shape:\n", y_train.shape)
# 打印出整个测试集输入特征的形状
print("x_test.shape:\n", x_test.shape)
# 打印出整个测试集标签的形状
print("y_test.shape:\n", y_test.shape)