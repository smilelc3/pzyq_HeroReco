import multiprocessing
import os
from img_class import PipeImg
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import time

# 读取图片转np
def read_img_to_np(path):
    img = mpimg.imread(path)
    return img

def consumer(pipe):
    output_p, input_p = pipe
    input_p.close()     # 关闭管道的输入端
    while True:
        try:
            item:PipeImg = output_p.recv()
        except EOFError:    # 管道内部无内容
            break
        # 处理项目
        plt.imshow(item.np_img)     # 可替换有用的工作
        plt.show()
        # print(item.create_time, pipe)
        # 关闭
        # print("Consumer close")


# 获取所有图片文件地址
def get_all_img_path(path)->list:
    result = []
    for root, _dirs, files in os.walk(path):
        for file in files:
            img_path = os.path.join(root, file)
            result.append(img_path)
    return result


# 生产项目并将其放置到队列上，sequence是代表要处理项目的可迭代对象
def producer(sequence: list, input_p: multiprocessing):
    for item in sequence:
        # 将项目放置在队列上
        img = read_img_to_np(item)
        input_p.send(PipeImg(img))


if __name__ == "__main__":
    time1 = time.time()

    (output_p,input_p) = multiprocessing.Pipe(duplex=True)
    # 启动使用者进程
    cons_p = multiprocessing.Process(target=consumer,args=((output_p,input_p),))
    cons_p.start()

    # 关闭生产者中的输出管道
    output_p.close()

    #生产项目
    sequence = get_all_img_path('单据扫描20180927')

    producer(sequence,input_p)

    # 关闭输入管道，表示完成
    input_p.close()

    # 等待使用者进程关闭
    cons_p.join()
    time2 = time.time()
    print(time2 - time1)
    #
    # time1 = time.time()
    # sequence = get_all_img_path('单据扫描20180927')
    # for file in sequence:
    #     item = PipeImg(read_img_to_np(file))
    #     plt.imshow(item.np_img)  # 可替换有用的工作
    #     plt.show()
    # time2 = time.time()
    # print(time2 - time1)