# coding: utf-8

import numpy as np
import os
from PIL import Image
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.optimizers import Adam
from keras.layers.normalization import BatchNormalization
from keras.utils import np_utils
from keras.layers import Conv2D, MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator
from keras.utils.vis_utils import plot_model

# %%加载自有数据
X_my = []
y_my = []
for root, dirs, files in os.walk(r'/home/test/tmp/pycharm_project_369/sql/图片数据库(标准化)'):
    for file in files:
        file_path = os.path.join(root, file)
        _root, num_dir = os.path.split(root)
        if num_dir.isdigit():
            print(file_path)
            img = Image.open(file_path)
            img = np.array(img.convert('L'))
            img_normalized = img / 255
            X_my.append(img_normalized)
            y_my.append(int(num_dir))

X_my = np.array(X_my)
X_my = X_my.reshape(X_my.shape[0], 28, 28, 1)

y_my = np.array(y_my)

# one-hot
number_of_classes = 10
Y_my = np_utils.to_categorical(y_my, number_of_classes)

# %%打乱数据集
per = np.random.permutation(y_my.shape[0])		#打乱后的行号
X_my = X_my[per, :, :]		#获取打乱后的训练数据
Y_my = Y_my[per, :]
print(X_my.shape, Y_my.shape)

#%%

np.random.seed(8)    #设置随机种子，保证每次随机数相同

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

X_train /= 255      # 归一化
X_test /= 255       # 归一化


number_of_classes = 10
# one-hot 转型
Y_train = np_utils.to_categorical(y_train, number_of_classes)
Y_test = np_utils.to_categorical(y_test, number_of_classes)


print("X_train original shape", X_train.shape)
print("X_test original shape", X_test.shape)
print("y_train original shape", y_train.shape)
print("y_test original shape", y_test.shape)
print("Y_train original shape", Y_train.shape)
print("Y_test original shape", Y_test.shape)

## 新数据构造方法
# 原来mnist train:6w, test:1w
# 6:1等分训练
X_train = np.append(X_train, X_my[0: X_my.shape[0] // 6 * 5, ], axis=0)
X_test = np.append(X_test, X_my[X_my.shape[0] // 6 * 5 + 1: , ], axis=0)
Y_train = np.append(Y_train, Y_my[0: Y_my.shape[0] // 6 * 5, ], axis=0)
Y_test = np.append(Y_test, Y_my[Y_my.shape[0] // 6 * 5 + 1: , ], axis=0)

# 三步卷积
# 1. 卷积
# 2. 激活
# 3. 池化
# 重复1，2，3步骤来添加更多中间隐藏层

# 4. 之后添加一层全连接层
# 借助全连接层实现CNN分类

model = Sequential()

model.add(Conv2D(filters=32, kernel_size=(3, 3), input_shape=(28, 28, 1))) # 输入28*28,1代表灰度
# 需训练的参数：3*3*1*32 + 32 = 320                        # 1代表输入深度
model.add(Activation('relu'))                           # relu激活
BatchNormalization(axis=1)                              # 批量标准化

model.add(Conv2D(filters=32, kernel_size=(3, 3)))       # 因采用3*3卷积核，正常卷积，输出dim(26-2)*(26-2)*32
# 需训练的参数：3*3*32* 32 + 32 = 9248                     # 32代表偏置

model.add(Activation('relu'))                           # relu激活

model.add(MaxPooling2D(pool_size=(2, 2)))               # max poling池化，di = 12*12*32
BatchNormalization(axis=1)                              # 归一化

model.add(Conv2D(filters=64, kernel_size=(3, 3)))
# 需训练的参数：3*3*32 * 64 + 64 = 18496

model.add(Activation('relu'))
BatchNormalization(axis=1)

model.add(Conv2D(filters=64, kernel_size=(3, 3)))
# 需训练的参数：3*3*64 * 64 + 64 = 36928
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
# Flatten层用来将输入“压平”，即把多维的输入一维化，常用在从卷积层到全连接层的过渡。Flatten不影响batch的大小。
BatchNormalization(axis=-1)
#压扁后的数据dim 4*4*64 = 1024

model.add(Dense(units=512))
# 需训练的参数：1024 * 512 + 512 = 524800
model.add(Dropout(0.2))

model.add(Activation('relu'))
BatchNormalization(axis=-1)

model.add(Dropout(0.2))

model.add(Dense(units=10))
# 需训练的参数：512 * 10 + 10 = 5130

# model.add(Convolution2D(10,3,3, border_mode='same'))
# model.add(GlobalAveragePooling2D())
model.add(Activation('softmax'))

model.summary()
# plot_model(model, to_file='model_keras_99-45.png', show_shapes=True, show_layer_names=False)

model.compile(loss='categorical_crossentropy', optimizer=Adam(), metrics=['accuracy'])

gen = ImageDataGenerator(rotation_range=8, width_shift_range=0.08, shear_range=0.3,
                         height_shift_range=0.08, zoom_range=0.08)

test_gen = ImageDataGenerator()


train_generator = gen.flow(X_train, Y_train, batch_size=64)
test_generator = test_gen.flow(X_test, Y_test, batch_size=64)

# model.fit(X_train, Y_train, batch_size=64, epochs=2, validation_data=(X_test, Y_test))

model.fit_generator(train_generator, steps_per_epoch=60000//64, epochs=10,
                    validation_data=test_generator, validation_steps=10000//64)

score = model.evaluate(X_test, Y_test)
print('Test accuracy: ', score[1])

model.save('model-99-45_add_my.h5')



