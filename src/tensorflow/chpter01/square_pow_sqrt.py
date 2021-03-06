import tensorflow as tf

a = tf.fill([1, 2], 3.0)
print("a-->", a)
# 平方
print(tf.square(a))
# 开方
print(tf.sqrt(a))
#