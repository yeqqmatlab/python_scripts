import tensorflow as tf

"""
Variable 可导 变量
"""
w = tf.Variable(tf.constant(5, dtype=tf.float32))
lr = 0.8
epoch = 40

"""
loss = (w+1)^2
dloss/dw = 2w+2
"""

"""
with ---> java try catch
"""
for ep in range(epoch):
    with tf.GradientTape() as tape:
        loss = tf.square(w+1)
    grads = tape.gradient(loss, w)

    w.assign_sub(lr*grads)  # w = w - lr*grads
    print("After %s epoch,w is %f,loss is %f" % (epoch, w.numpy(), loss))


