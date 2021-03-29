import tensorflow as tf
import numpy as np

SEED = 222

rdm = np.random.RandomState(seed=SEED)
x = rdm.rand(32, 2)
# print(x)

y_dest = [[2 * x1 + 5*x2 + (rdm.rand() / 10.0 - 0.05)] for (x1, x2) in x]
print(y_dest)

x = tf.Variable(x, dtype=tf.float32)

w1 = tf.Variable(tf.random.normal([2, 1], stddev=1, seed=1))

lr = 0.00115

LR_BASE = 0.002

LR_DECAY = 0.98 # 学习率衰减率

LR_STEP = 1  # 喂了多少轮BATCH_SIZE后，更新一次学习率

for epoch in range(15000):

    # lr = LR_BASE * LR_DECAY ** (epoch / (LR_STEP*100))

    with tf.GradientTape() as tape:

        y_pred = tf.matmul(x, w1)
        loss_mse = tf.reduce_mean(tf.square(y_dest - y_pred))

    grads = tape.gradient(loss_mse, w1)
    w1.assign_sub(lr * grads)

    if epoch % 500 == 0:
        print("lr-->", lr)
        print("After %d training steps,w1 is " % (epoch))
        print(w1.numpy(), "\n")

print("final w1 is: ", w1.numpy())
