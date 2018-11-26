# author: smile
# coding: utf-8

import matplotlib.pyplot as plt
import numpy as np
import cv2

# 基于扫描线的算法
def scan_line_method(img: np.ndarray)-> np:
    gray = cv2.cvtColor(np.asarray(img),cv2.COLOR_RGB2GRAY)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    horsum, versum = get_image_horizontal_and_vertical_sum(binary)
    # 图像展示
    # display_horizontal_and_vertical_result(horsum, versum, gray)
    # cv2.imshow('二值化', binary)

    # 定义滑动窗口相关参数
    win_size = 5                # 窗口大小
    move_step = 2               # 每步滑动大小
    min_rate_threshold = 0.66   # 保证必须大于最速下降的0.66
    xmin = ymin = 0
    ymax, xmax = img.shape[:2]

    # TODO 可以尝试并行运算
    # 计算横向(左)
    line_scan_result = []
    for start_index in range(0, len(horsum) // 2 - win_size, move_step):
        current_win = horsum[start_index: start_index + win_size]
        current_win_val = 0
        for index, val in enumerate(current_win[:-1]):
            current_win_val += val - current_win[index + 1]
        line_scan_result.append(current_win_val)
    # print(line_scan_result)
    line_scan_result.reverse()
    if max(line_scan_result) > len(versum) * min_rate_threshold:
        xmin = max(xmin, (len(line_scan_result) - line_scan_result.index(max(line_scan_result)) - 1) * move_step + win_size)
    line_scan_result.reverse()
    # print('xmin =', xmin, max(line_scan_result))

    # 计算横向(右)
    line_scan_result = []
    for start_index in range(len(horsum) // 2, len(horsum), move_step):
        current_win = horsum[start_index: start_index + win_size]
        current_win_val = 0
        for index, val in enumerate(current_win[:-1]):
            current_win_val += val - current_win[index + 1]
        line_scan_result.append(current_win_val)
    # print(line_scan_result)
    line_scan_result.reverse()
    if min(line_scan_result) < -len(versum) * min_rate_threshold:
        xmax = min(xmax, len(horsum) // 2 + (len(line_scan_result) - line_scan_result.index(min(line_scan_result)) - 1) * move_step)
    line_scan_result.reverse()
    # print('xmax =', xmax, min(line_scan_result))


    # 计算纵向(上)
    line_scan_result = []
    for start_index in range(0, len(versum) // 2 - win_size, move_step):
        current_win = versum[start_index: start_index + win_size]
        current_win_val = 0
        for index, val in enumerate(current_win[:-1]):
            current_win_val += val - current_win[index + 1]
        line_scan_result.append(current_win_val)
    # print(line_scan_result)
    line_scan_result.reverse()
    if max(line_scan_result) > len(horsum) * min_rate_threshold:
        ymin = max(ymin, (len(line_scan_result) - line_scan_result.index(max(line_scan_result)) - 1) * move_step + win_size)
    line_scan_result.reverse()
    # print('ymin =', ymin)

    # 计算纵向(下)
    line_scan_result = []
    for start_index in range(len(versum) // 2, len(versum), move_step):
        current_win = versum[start_index: start_index + win_size]
        current_win_val = 0
        for index, val in enumerate(current_win[:-1]):
            current_win_val += val - current_win[index + 1]
        line_scan_result.append(current_win_val)
    # print(line_scan_result)
    line_scan_result.reverse()
    if min(line_scan_result) < -len(horsum) * min_rate_threshold:
        ymax = min(ymax, len(versum) // 2 + (len(line_scan_result) - line_scan_result.index(min(line_scan_result)) - 1) * move_step)
    line_scan_result.reverse()
    # print('ymax =', ymax)

    return img[ymin: ymax, xmin: xmax]



# 横向、纵向像素统计
def get_image_horizontal_and_vertical_sum(image):
    rows, cols = image.shape
    horsum = []
    versum = []
    for i in range(cols):
        val = (255 - np.array(image[:, i]).sum()) / 255
        horsum.append(val)
    for i in range(rows):
        val = (255 - np.array(image[i, :]).sum()) / 255
        versum.append(val)
    horsum = horsum - min(horsum)
    versum = versum - min(versum)
    return horsum, versum


# 用于展示像素分布结果
def display_horizontal_and_vertical_result(horsum, versum, img):
    plt.title('Result Analysis')
    plt.subplot(311), plt.plot(range(len(horsum)), horsum, color='green')
    plt.xlim(0, len(horsum) - 1)
    plt.xlabel('pixel')
    plt.ylabel('hor sum')
    plt.subplot(312), plt.plot(range(len(versum)), versum, color='red')
    plt.xlim(0, len(versum) - 1)
    plt.xlabel('pixel')
    plt.ylabel('ver sum')
    plt.subplot(313), plt.hist(img.ravel(), 256)
    plt.xlim(0, 255)

    plt.show()

if __name__ == '__main__':
    import os
    for root, dirs, files in os.walk(r'C:\Users\smile\PycharmProjects\pzyq_HeroReco\sql\图片数据库\会员编号\1'):
        for file in files:
            # print(root + '\\' + file)
            img = plt.imread(root + '\\' + file)
            cv2.imshow('result', scan_line_method(img))
            cv2.waitKey(100)
        # img = plt.imread(root + '\\' + files[9])
        # cv2.imshow('result', scan_line_method(img))
        # cv2.waitKey(0)