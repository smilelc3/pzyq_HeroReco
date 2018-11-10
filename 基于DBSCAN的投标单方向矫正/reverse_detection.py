import cv2
import 基于DBSCAN的投标单方向矫正.const as const
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import DBSCAN
import datetime
import os

# 耗时装饰器
def count_time(func):
    def int_time(*args, **kwargs):
        start_time = datetime.datetime.now()  # 开始时间
        func(*args, **kwargs)
        over_time = datetime.datetime.now()   # 结束时间
        total_time = (over_time-start_time).total_seconds()
        print(f'func #{func.__name__}# cost %s s' % total_time)
    return int_time

class Dec(object):
    def __init__(self, binaryMethod='Otsu'):
        self.isImgCheck = False
        self.binaryMethod = binaryMethod
        self.needReverse = False    # 是否需要翻转
        self.rawImg = []

    #@count_time
    def set_img_from_file(self, file):
        self.rawImg = cv2.imread(file)
        self.isImgCheck = True
        self.needReverse = False
        self._resize_and_binary()

    #@count_time
    def set_img_from_np(self, Img):
        self.needReverse = False
        self.isImgCheck = True
        self.rawImg = Img
        self._resize_and_binary()

    def _resize_and_binary(self):
        self.preProcessImg = cv2.cvtColor(self.rawImg, cv2.COLOR_BGR2GRAY)
        self.preProcessImg = cv2.resize(self.preProcessImg,
                                        dsize=None,
                                        fx=const.RESIZE_PER,            # 指定长宽比放缩
                                        fy=const.RESIZE_PER,
                                        interpolation=cv2.INTER_NEAREST)   # 采用最快的临近插值算法
        if self.binaryMethod == 'Otsu':
            _ret, self.preProcessImg = cv2.threshold(self.preProcessImg, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        elif self.binaryMethod == 'Simple':
            _ret, self.preProcessImg = cv2.threshold(self.preProcessImg, 127 - const.THRESHOLD_OFFSET, 255, cv2.THRESH_BINARY)
        else:
            self.isImgCheck = False
            print('please set correct binaryMethod param, only suport Otsu or Simple')
            return

    #@count_time
    def get_corect_img_np(self)-> np:       # 返回翻转后np类型数据
        if self.isImgCheck == False:
            return

        self._X = [[x, y] \
             for x in range(self.preProcessImg.shape[0]) for y in range(self.preProcessImg.shape[1])  \
             if self.preProcessImg[x][y] == 255]

        db = DBSCAN(eps=const.DBSCAN_EPS, min_samples=const.DBSCAN_MINP).fit(self._X)     # DBSCAN
        self._labels = db.labels_
        self.n_clusters = len(set(self._labels)) - (1 if -1 in self._labels else 0)

        self.totalDot = 0
        self.illegalDot = 0
        for index, val in enumerate(self._labels):
            if val != 0:  # 有效点统计
                self.totalDot += 1
                #print(X[index])
                if  self.preProcessImg.shape[0] / 6 < self._X[index][0] and \
                    self.preProcessImg.shape[0] / 3 > self._X[index][1]:   # 在左下角数量
                    self.illegalDot += 1

        # 置信度计算

        if self.totalDot == 0:
            self.resultImg = self.rawImg
        elif self.illegalDot / self.totalDot > const.PER_THRES / 100:         # 小于百分比阈值
            print('sig: %.2f' % (self.illegalDot / self.totalDot * 100))
            self.needReverse = True
            self.resultImg = cv2.flip(self.rawImg, -1)          # 图像水平垂直翻转
        else:
            self.resultImg = self.rawImg

        return self.resultImg

    def show_figure_result(self):   #图展示结果
        plt.subplot(221)
        plt.title('raw img')
        plt.imshow(self.rawImg)     # 原图

        plt.subplot(222)
        plt.title('binary img')
        plt.imshow(self.preProcessImg, cmap='gray')  # 二值化图像

        plt.subplot(223)            # 标记点

        plt.imshow(self.preProcessImg, cmap='gray')
        unique_labels = set(self._labels)
        colors = [plt.cm.Spectral(each)
                  for each in np.linspace(0, 1, len(unique_labels))]

        for k, col in zip(unique_labels, colors):
            if k == -1:
                # Black used for noise.
                col = [1, 1, 0, 1]

            class_member_mask = (self._labels == k)
            xy = [self._X[index] for index, val in enumerate(class_member_mask) if val]
            # print(xy)
            if len(xy) > 500:
                continue
            for dot in xy:
                plt.plot(dot[1], dot[0], 'o', markerfacecolor=tuple(col), markeredgecolor='y', markersize=5)

        plt.xlim((0, self.preProcessImg.shape[1]))
        plt.ylim((0, self.preProcessImg.shape[0]))
        plt.axis([0, self.preProcessImg.shape[1], self.preProcessImg.shape[0], 0])
        plt.title('Estimated number of clusters: %d' % self.n_clusters)

        plt.subplot(224)        # 翻转结果
        plt.title('result img')
        plt.imshow(self.resultImg)
        plt.show()

# 获取所有图片文件地址
def get_all_img_path(path)->list:
    result = []
    for root, _dirs, files in os.walk(path):
        for file in files:
            img_path = os.path.join(root, file)
            result.append(img_path)
    return result


if __name__ == '__main__':

    identify = Dec(binaryMethod='Otsu')
    file_list = get_all_img_path('../单据扫描20180927')
    print(file_list)
    for file in file_list:
        identify.set_img_from_file(file)
        img = identify.get_corect_img_np()
        #print(identify.needReverse)  # 记录是否需要翻转
        if identify.needReverse == True:
            print(file)
            identify.show_figure_result()       # 图片展示
