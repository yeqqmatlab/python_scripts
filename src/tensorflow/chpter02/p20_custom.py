import tensorflow as tf
import numpy as np

SEED = 2345

COST = 1
PROFIT = 99

rdm = np.random.RandomState(SEED)

x = rdm.rand(32, 2)
#
y = [[x1 + x2 + (rdm.rand() / 10.0 - 0.05)] for (x1, x2) in x]
print("---------x---------")
print(x)
print("---------y---------")
print(y)

x = tf.cast(x, dtype=tf.float32)
# y_ = tf.cast(y_, dtype=tf.float32)

w1 = tf.Variable(tf.random.normal([2, 1], stddev=1, seed=1))

epoch = 10000
lr = 0.002

for i in range(epoch):
    with tf.GradientTape() as tape:
        y_pred = tf.matmul(x, w1)
        """
        预测大了
        y_pred > y --> (y_pred - y)*(y_pred - y) * 1 正常误差
        预测小了
        y_pred < y --> (y_pred - y)*(y_pred - y) * 99 放大误差
        """
        loss = tf.reduce_mean(tf.where(tf.greater(y_pred, y), (y_pred - y)*(y_pred - y) * 1, (y_pred - y)*(y_pred - y) * 99))
        # loss = tf.reduce_mean(tf.square(y-y_))

    grads = tape.gradient(loss, w1)
    w1.assign_sub(lr * grads)

    if epoch % 500 == 0:
        print("after %d training step, w1 is " % (i))
        print(w1.numpy())

print("Final w1 is : ", w1.numpy())

# 自定义损失函数
# 酸奶成本1元,利润99元
# 成本低，利润高，人们希望多预测些，生成模型系数大于1，往多了预测
