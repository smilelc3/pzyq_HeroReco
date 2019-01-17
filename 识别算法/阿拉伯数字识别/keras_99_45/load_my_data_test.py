# coding: utf-8

import numpy as np
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
from keras.models import load_model
import os
from PIL import Image


X_test = []
y_test = []

for root, dirs, files in os.walk(r'/home/test/tmp/pycharm_project_369/sql/图片数据库(标准化)'):
    for file in files:
        file_path = os.path.join(root, file)
        _root, num_dir = os.path.split(root)
        if num_dir.isdigit():
            print(file_path)
            img = Image.open(file_path)
            img = np.array(img.convert('L'))
            img_normalized = img / 255
            X_test.append(img_normalized)
            y_test.append(int(num_dir))

X_test = np.array(X_test)
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)

y_test = np.array(y_test)

number_of_classes = 10
Y_test = np_utils.to_categorical(y_test, number_of_classes)

print(X_test.shape, y_test.shape)
print(Y_test[0])



# 载入模型
model = load_model('model-99-45_add_my.h5')
# 评估模型
loss,accuracy = model.evaluate(X_test, Y_test)

print('test loss',loss)
print('accuracy',accuracy)