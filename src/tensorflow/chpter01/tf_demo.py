import tensorflow as tf

a = tf.constant([[1, 4], [5, 6], [5, 9]], dtype=tf.int64)
"""
demo
hello

"""
print("a:", a)
print("a.dtype:", a.dtype)
print("a.shape", a.shape)

print(help(tf.constant))
