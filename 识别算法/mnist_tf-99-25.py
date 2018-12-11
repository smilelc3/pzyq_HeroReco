from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

# 获取数据集
mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)

# 定义输入和输出的占位符
x = tf.placeholder(tf.float32, [None, 784])
y_ = tf.placeholder(tf.float32, [None, 10])

# 定义通用函数
def weight_variable(shape):
    # 截断正态分布 标准方差为0.1
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

def bias_variable(shape):
    # 设为非零避免死神经元
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)

def conv2d(x, W):
    # 卷积不改变输入的shape
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],
                          strides=[1, 2, 2, 1], padding='SAME')

sess = tf.InteractiveSession()

# 构建模型

# 把输入变换成一个4d的张量，第二三个对应的是图片的长和宽，第四个参数对应的颜色
x_image = tf.reshape(x, [-1, 28, 28, 1])

# 计算32个特征，每5*5patch,第一二个参数指的是patch的size，第三个参数是输入的channels，第四个参数是输出的channels
W_conv1 = weight_variable([5, 5, 1, 32])
# 偏差的shape应该和输出的shape一致，所以也是32
b_conv1 = bias_variable([32])

# 28*28的图片卷积时步长为1，随意卷积后大小不变，按2*2最大值池化，相当于从2*2块中提取一个最大值，
# 所以池化后大小为[28/2,28/2] = [14,14]，第二次池化后为[14/2,14/2] = [7,7]

# 对数据做卷积操作
h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
# max_pool_2x2之后，图片变成14*14
h_pool1 = max_pool_2x2(h_conv1)

# 在以前的基础上，生成了64个特征
W_conv2 = weight_variable([5, 5, 32, 64])
b_conv2 = bias_variable([64])

h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
# max_pool_2x2之后，图片变成7*7
h_pool2 = max_pool_2x2(h_conv2)

# 构造一个全连接的神经网络，1024个神经元
W_fc1 = weight_variable([7 * 7 * 64, 1024])
b_fc1 = bias_variable([1024])
# 输出为1024
h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

# 做Dropout操作
keep_prob = tf.placeholder(tf.float32)
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])

y_conv = tf.matmul(h_fc1_drop, W_fc2) + b_fc2

# 定义损失函数
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y_conv))
# 定义优化函数
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
# 计算准确率
correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
# 初始化参数
sess.run(tf.global_variables_initializer())
for i in range(20000):
    batch = mnist.train.next_batch(50)
    if i % 100 == 0:
        train_accuracy = accuracy.eval(feed_dict={x: batch[0], y_: batch[1], keep_prob: 1.0})
        print("step %d, training accuracy %g" % (i, train_accuracy))
    train_step.run(feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.5})

print("test accuracy %g" % accuracy.eval(feed_dict={
    x: mnist.test.images, y_: mnist.test.labels, keep_prob: 1.0}))


