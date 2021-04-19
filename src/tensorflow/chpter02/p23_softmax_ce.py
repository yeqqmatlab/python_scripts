# softmax与交叉熵损失函数结合
import tensorflow as tf
import numpy as np

"""
softmax 归一化指数函数
arr=[12,5,8]
softmax(arr[i]) = tf.exp(arr[i]) / tf.reduce_sum(tf.exp(arr))
"""

y_ = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 0, 0], [0, 1, 0]])
y = np.array([[12, 3, 2], [3, 10, 1], [1, 2, 5], [4, 6.5, 1.2], [3, 6, 1]])

y_pro = tf.nn.softmax(y)
print(y_pro)
print(tf.reduce_sum(y_pro, axis=1))  # tf.Tensor([1. 1. 1. 1. 1.], shape=(5,), dtype=float64)

loss_ce1 = tf.losses.categorical_crossentropy(y_, y_pro)

loss_ce2 = tf.nn.softmax_cross_entropy_with_logits(y_, y)
print("---------------")
# 其中 loss_ce1[3] 值最大，说明概率分布相似度小
print(loss_ce1[3])
print("---------------")
print(loss_ce2)


