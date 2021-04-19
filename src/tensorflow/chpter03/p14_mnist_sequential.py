import tensorflow as tf

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# 归一化处理
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
              metrics=['sparse_categorical_accuracy'])

# 添加
# windows 打开cmd 执行 tensorboard --logdir E:/python_workspace/python_scripts/log/fit --host 0.0.0.0 --port 8080
# http://localhost:8080
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir="E:/python_workspace/python_scripts/log/fit")

model.fit(x_train, y_train,
         # batch_size=32,
          epochs=5,
          validation_data=(x_test, y_test),
          validation_freq=1,
          callbacks=[tensorboard_callback])
model.summary()
