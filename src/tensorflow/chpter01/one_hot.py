import tensorflow as tf

classes = 3
labels = tf.constant([1, 0, 2])
output = tf.one_hot(labels, depth=classes)
print("result of labels1:", output)
