# 交叉熵误差函数

import tensorflow as tf

"""
交叉熵损失函数表示二个概率分布之间的距离（个人认为相似度更合适），交叉熵越小说明二者分布越接近，是分类问题中使用较为广泛的损失函数。
概率分布
[1, 0]
[0.6, 0.4]
H(y_,y) = -累加(y_*lny)
其中y_代表数据的真实值，y代表神经网络预测值
loss_ce1 = -1*ln0.6-0*ln0.4 = 0.5108256
loss_ce2 = -1*ln0.8-0*ln0.2 = 0.2231435

"""
loss_ce1 = tf.losses.categorical_crossentropy([1, 0], [0.6, 0.4])
loss_ce2 = tf.losses.categorical_crossentropy([1, 0], [0.8, 0.2])

print(loss_ce1)
print(loss_ce2)