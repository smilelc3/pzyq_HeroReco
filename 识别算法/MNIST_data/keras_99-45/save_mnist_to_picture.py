# coding: utf-8

from tensorflow.examples.tutorials.mnist import input_data
import scipy.misc
import os
import numpy as np

# 读取MNIST数据集。如果不存在会事先下载。
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# 我们把原始图片保存在MNIST_data/raw/文件夹下
# 如果没有这个文件夹会自动创建
save_dir = 'MNIST_data/raw/'
if os.path.exists(save_dir) is False:
    os.makedirs(save_dir)

# # 保存train图片
for i in range(mnist.train.num_examples):
    # 请注意，mnist.train.images[i, :]就表示第i张图片（序号从0开始）
    image_array = mnist.train.images[i, :]
    # TensorFlow中的MNIST图片是一个784维的向量，我们重新把它还原为28x28维的图像。
    image_array = image_array.reshape(28, 28)
    # 保存文件的格式为 mnist_train_0.jpg, mnist_train_1.jpg, ... ,mnist_train_19.jpg
    image_label = mnist.train.labels[i, :]
    sub_folder = str(int(np.where(image_label == 1)[0]))
    filename_path = os.path.join(save_dir, 'train', sub_folder)
    # 将image_array保存为图片
    # 先用scipy.misc.toimage转换为图像，再调用save直接保存。
    if os.path.exists(filename_path) is False:
        os.makedirs(filename_path)
    print(os.path.join(filename_path, 'mnist_train_%d.jpg' % i))
    scipy.misc.toimage(image_array, cmin=0.0, cmax=1.0).save(os.path.join(filename_path, 'mnist_train_%d.jpg' % i))

# 保存test图片
for i in range(mnist.test.num_examples):
    image_array = mnist.test.images[i, :]
    image_array = image_array.reshape(28, 28)
    image_label = mnist.test.labels[i, :]
    sub_folder = str(int(np.where(image_label == 1)[0]))
    filename_path = os.path.join(save_dir, 'test', sub_folder)
    if os.path.exists(filename_path) is False:
        os.makedirs(filename_path)
    print(os.path.join(filename_path, 'mnist_train_%d.jpg' % i))
    scipy.misc.toimage(image_array, cmin=0.0, cmax=1.0).save(os.path.join(filename_path, 'mnist_train_%d.jpg' % i))

print('Please check: %s ' % save_dir)