# coding = utf-8

import numpy as np
import os
from PIL import Image
from keras.utils import np_utils
from HCCR_CNN9Layer import hwdb_model
from keras.utils.vis_utils import plot_model
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
import h5py
import json
import time
from keras.callbacks import TensorBoard
from keras.callbacks import ModelCheckpoint

np.random.seed(888)   # 设置随机种子
IMG_SIZE = 96

os.environ['CUDA_VISIBLE_DEVICES'] = '0'

zh_to_label: dict = json.loads(open('zh_to_label.json', 'r').read())
HWDB_h5_file = r'C:\Users\smile\PycharmProjects\HWDB_DL\HWDB1.0-1.1.hdf5'

f = h5py.File(HWDB_h5_file, 'r')

X_train = f['X_train']
Y_train = f['Y_train']
X_test = f['X_test']
Y_test = f['Y_test']

train_num = 2678424
test_num = 224419

batch_size = 128

model = hwdb_model(IMG_SIZE, len(zh_to_label))
# model.summary()

# 展示模型
#os.environ["PATH"] += r'C:\Program Files (x86)\Graphviz2.38\bin' + os.pathsep
#plot_model(model, to_file='model_HWDB_change.png', show_shapes=True, show_layer_names=False)


def generator(h5_X, h5_Y, indices, batchSize):
    while True:
        np.random.shuffle(indices)
        for i in range(0, len(indices), batchSize):
            t0 = time.time()
            #batch_indices = indices[i:i+batchSize]
            #batch_indices.sort()
            # print(batch_indices)

            bx = h5_X[i:i+batchSize] / 255
            by = h5_Y[i:i+batchSize]
            bx.reshape((batch_size, 96, 96, 1))
            t1 = time.time()
            print(f'batchSize = {batchSize}, spendTime={t1-t0}')
            # print(bx.shape)
            yield (bx, by)


train_generator = generator(X_train, Y_train, indices=[i for i in range(train_num)], batchSize=batch_size)
test_generator = generator(X_test, Y_test, indices=[i for i in range(test_num)], batchSize=batch_size)

#tensorboad = TensorBoard(log_dir='log')
#checkpoint = ModelCheckpoint(filepath='weights.{epoch:02d}-{val_acc:.2f}.hdf5', monitor='val_acc', mode='auto', save_best_only='True')

# model.fit(
#     X_train, Y_train,
#     batch_size=256, epochs=20,
#     validation_data=(X_test, Y_test),
#     shuffle="batch",
#     callbacks=[tensorboad, checkpoint]
# )

model.fit_generator(
    train_generator,
    steps_per_epoch=train_num//batch_size,
    epochs=50,
    validation_data=test_generator,
    validation_steps=test_num//batch_size,
)

score = model.evaluate(X_test, Y_test, verbose=0)
print('Test accuracy: ', score)

model.save('model_HWDB_change.h5')