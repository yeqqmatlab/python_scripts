import tensorflow as tf

a = tf.constant([1, 2, 3, 1, 1])
b = tf.constant([0, 1, 3, 4, 5])
# 若 a > b,返回a对应的位置元素, 否则返回b对应的位置元素
c = tf.where(tf.greater(a, b), a, b)

print(c)
