from PIL import Image
import numpy as np
import tensorflow as tf

# model_save_path = './checkpoint/mnist.ckpt'

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
              metrics=['sparse_categorical_accuracy'])

model.fit(x_train, y_train, batch_size=32, epochs=5, validation_data=(x_test, y_test), validation_freq=1)
model.summary()
    
# model.load_weights(model_save_path)

# preNum = int(input("input the number of test pictures:"))


image_path = './8.png'
img = Image.open(image_path)
img = img.resize((28, 28), Image.ANTIALIAS)
img_arr = np.array(img.convert('L'))

img_arr = 255 - img_arr

img_arr = img_arr / 255.0
print("img_arr:",img_arr.shape)
x_predict = img_arr[tf.newaxis, ...]
print("x_predict:",x_predict.shape)
result = model.predict(x_predict)

pred = tf.argmax(result, axis=1)

print('\n')
tf.print(pred)
