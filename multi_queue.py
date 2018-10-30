
import os
from img_class import PipeImg
from multiprocessing import Process, Queue, Event
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import time

# 设置队列最大容许长度，避免可能超内存
MAX_QUEUE_SIZE = 50

# 读取图片转np
def read_img_to_np(path):
    img = mpimg.imread(path)
    return img


# 获取所有图片文件地址
def get_all_img_path(path)->list:
    result = []
    for root, _dirs, files in os.walk(path):
        for file in files:
            img_path = os.path.join(root, file)
            result.append(img_path)
    return result

# 写数据进程执行的代码:
def producer(queue:Queue, event:Event):
    event.set()         # 设置进程启动，进入运行状态
    for item in get_all_img_path('单据扫描20180927'):
        img = read_img_to_np(item)
        while queue.qsize() >= MAX_QUEUE_SIZE:
            event.wait()    # 超过最大队列数，等待
        queue.put(PipeImg(img))
    event.clear()       # 停止运行 进入阻塞状态


# 读数据进程执行的代码:
def consumer(queue:Queue, event:Event):
    while True:
        print('Queue size:', queue.qsize(), '写入进程运行中?', event.is_set())
        if not queue.empty():
            item: PipeImg = queue.get()
            plt.imshow(item.np_img)
            plt.show()
        elif event.is_set() == False:   # 如果队列空且生产者已阻塞，认为已完成
            print('done!')
            return

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    img_queue = Queue()
    img_event = Event()
    input_q = Process(target=producer, args=(img_queue,img_event))
    output_q = Process(target=consumer, args=(img_queue,img_event))

    # 启动子进程input_q，写入:
    input_q.start()
    # 启动子进程output_q，读取:
    output_q.start()

    # 等待结束
    input_q.join()
    output_q.join()

