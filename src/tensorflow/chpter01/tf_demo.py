import tensorflow as tf

a = tf.constant([[1, 4], [5, 6], [5, 9]], dtype=tf.int64)

print("a:", a)
print("a.dtype:", a.dtype)
print("a.shape", a.shape)
