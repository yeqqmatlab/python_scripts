import tensorflow as tf

w = tf.Variable(tf.constant(5,dtype=tf.float32))

# epoch = 40

LR_BASE = 0.2

LR_DECAY = 0.99 # 学习率衰减率

LR_STEP = 1  # 喂了多少轮BATCH_SIZE后，更新一次学习率

for epoch in range(50):
    lr = LR_BASE * LR_DECAY ** (epoch/LR_STEP)
    with tf.GradientTape() as tape:
        loss = tf.square(w + 1)
    grades = tape.gradient(loss, w)

    w.assign_sub(lr*grades)
    print("epoch-->", epoch)
    print("After %s epoch,w is %f,loss is %f,lr is %f" % (epoch, w.numpy(), loss, lr))


