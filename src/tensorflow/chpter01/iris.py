# 利用鸢尾花数据集，实现简单的神经网络

# 导入所需要的模块
from sklearn.datasets import load_iris
from matplotlib import pyplot as plt
import numpy as np
import tensorflow as tf

# 导入数据,分别为输入特征矩阵和标签
data_iris = load_iris()
x_data = data_iris.data   # 特征矩阵
y_data = data_iris.target  # 标签

# 随机打乱数据（因为原始数据是顺序的，顺序不打乱会影响准确率）
# seed: 随机数种子，是一个整数，当设置之后，每次生成的随机数都一样（为方便教学，以保每位同学结果一致）
np.random.seed(116)  # 使用相同的seed，保证输入特征和标签一一对应
np.random.shuffle(x_data)
np.random.seed(116)
np.random.shuffle(y_data)
tf.random.set_seed(116)

# print(x_data)
# print(y_data)

x_train = x_data[:-30]
y_train = y_data[:-30]

x_test = x_data[-30:]
y_test = y_data[-30:]

# print("y_test--->", y_test)

# 转化为tf的数据类型
x_train = tf.cast(x_train, tf.float32)
x_test = tf.cast(x_test, tf.float32)

# 批处理
train_db = tf.data.Dataset.from_tensor_slices((x_train, y_train)).batch(30)
test_db = tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(30)

w1 = tf.Variable(tf.random.truncated_normal([4, 3], stddev=0.1, seed=1))
b1 = tf.Variable(tf.random.truncated_normal([3], stddev=0.1,  seed=1))

lr = 0.1  # 学习率

train_loss_results = []   # 将每轮的loss记录在此列表中, 为后续画loss曲线提供数据
test_acc = []    #  将每轮的acc记录在此列表中, 为后续画acc曲线提供数据
epoch = 500
loss_all = 0   #  每轮分4个step, loss_all记录四个step生成的4个loss的和

#  训练部分
for ep in range(epoch):
    for step, (step_x_train, step_y_train) in enumerate(train_db):
        with tf.GradientTape() as tape:
            y = tf.matmul(step_x_train, w1) + b1
            y = tf.nn.softmax(y)
            y_one_hot = tf.one_hot(step_y_train, depth=3)
            loss = tf.reduce_mean(tf.square(y_one_hot - y))
            loss_all += loss.numpy()

        # 对 loss 求导
        grads = tape.gradient(loss, [w1, b1])

        # 迭代更新 w1 = w1 - lr*w1_grad   b = b - lr*b_grad
        w1.assign_sub(lr*grads[0])
        b1.assign_sub(lr*grads[1])

    # 每个epoch，打印loss信息
    print("Epoch {}, loss: {}".format(ep, loss_all / 4))
    train_loss_results.append(loss_all / 4)  # 将4个step的loss求平均记录在此变量中
    loss_all = 0  # loss_all归零，为记录下一个epoch的loss做准备

    # 测试部分
    # total_correct为预测[对]的样本个数, total_number为测试的总样本数，将这两个变量都初始化为0
    total_correct, total_number = 0, 0
    for x_test, y_test in test_db:
        #  使用更新后的参数进行预测
        y = tf.matmul(x_test, w1) + b1
        y = tf.nn.softmax(y)
        print("y--->", y)
        pred = tf.argmax(y, axis=1)  #  返回每一行最大的索引
        pred = tf.cast(pred, dtype=y_test.dtype)
        print("pred----->", pred)
        print("y_test--->", y_test)
        correct = tf.cast(tf.equal(pred, y_test), dtype=tf.int32)
        correct = tf.reduce_sum(correct)
        total_correct += int(correct)
        # total_number为测试的总样本数 ,即测试数据集行数
        total_number += x_test.shape[0]

    print("total_correct", total_correct)
    print("total_number", total_number)
    acc = total_correct / total_number
    print("acc", acc)
    test_acc.append(acc)
    print(" Test_acc-------------->", acc)

# 绘制 loss 曲线
plt.title(' Loss Function Curve ')  #  图片标题
plt.xlabel('Epoch')   #  x轴变量名称
plt.ylabel('Loss')    #  y轴变量名称
plt.plot(train_loss_results, label="$Loss$")  # 逐点画出trian_loss_results值并连线，连线图标是Loss
plt.legend()
plt.show()

# 绘制 Accuracy 曲线
plt.title('Acc Curve')  # 图片标题
plt.xlabel('Epoch')  # x轴变量名称
plt.ylabel('Acc')  # y轴变量名称
plt.plot(test_acc, label="$Accuracy$")  # 逐点画出test_acc值并连线，连线图标是Accuracy
plt.legend()
plt.show()

print("w1", w1)
print("b1", b1)


























