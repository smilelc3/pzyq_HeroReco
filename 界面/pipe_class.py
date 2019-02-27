# coding: utf-8

# 管道通信类

import os
import time
from multiprocessing import Process, Queue, Event
from keras.models import load_model as keras_load_model
from matplotlib import pyplot as plt

class PipeImg:
    def __init__(self):
        self.MAX_QUEUE_SIZE = 100       # 定义队列最大长度
        self.queue_size = 0
        # 创建消息队列和事件队列
        self._create_img_queue()
        self._start_img_queue()


    # 对用户开放 加载一张图片
    def load_one_image(self, img_path):
        img = plt.imread(img_path)
        self.img_producer(self.img_queue, self.img_event, img)


    # 对用户开放 加载图片文件夹，仅仅支持常用图片后缀 jpg, png, jpeg, bmp
    def load_images_folder(self, folder_path, support_suffix=('jpg', 'png', 'jpeg', 'bmp') ):
        for root, _dirs, files in os.walk(folder_path):
            for file in files:
                _, extension = os.path.splitext(file)
                if extension not in support_suffix:
                    continue
                img_path = os.path.join(root, file)
                img = plt.imread(img_path)
                self.img_producer(self.img_queue, self.img_event, img)


    # 图片加载进程
    def img_producer(self, queue:Queue, event:Event, img=None):
        event.set()                                 # 设置进程启动
        while queue.qsize() >= self.MAX_QUEUE_SIZE:
            event.wait()  # 超过最大队列数，等待
        if img != None:
            queue.put(img)
            print('压入图片')
            self.queue_size = queue.qsize()


    # 图片处理进程
    def img_consumer(self,queue:Queue, event:Event):
        while True:
            print('Queue size:', queue.qsize(), '写入进程运行中?', event.is_set())
            if not queue.empty():
                img = queue.get()
                plt.imshow(img)
                plt.show()
            elif self.img_event.is_set() == False:  # 如果队列空且生产者已阻塞，认为已完成
                print('done!')
                return

    # 创建进程
    def _create_img_queue(self):
        self.img_queue = Queue()
        self.img_event = Event()
        self.enqueue = Process(target=self.img_producer, args=(self.img_queue, self.img_event))
        self.dequeue = Process(target=self.img_consumer, args=(self.img_queue, self.img_event))

    # 开始进程
    def _start_img_queue(self):
        self.enqueue.start()
        self.dequeue.start()

        self.enqueue.join()
        self.dequeue.join()

    # 结束进程
    def stop_img_queue(self):
        self.img_event.clear()
        self.img_queue.close()


    #  加载小写数字模型
    def load_num_model(self, model_path: str):
        self.num_model = keras_load_model(model_path)
        self.num_model_path = model_path

    # TODO
    def load_NUM_model(self):
        pass

if __name__ == '__main__':
    pipe_test = PipeImg()
    pipe_test.load_num_model(r'C:\Users\smile\PycharmProjects\pzyq_HeroReco\识别算法\阿拉伯数字识别\keras_99_45\model-99-45_add_my.h5')
    pipe_test.load_one_image(r'C:\Users\smile\PycharmProjects\pzyq_HeroReco\sql\人工填写20181122\0001.jpg')
