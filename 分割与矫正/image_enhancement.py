# coding=utf-8


# 使用膨胀 和 求 最长连续子区间 算法
import cv2
from 分割与矫正.remove_black_border import get_image_horizontal_and_vertical_sum
from matplotlib import pyplot as plt
import numpy as np



def get_main_part(img: np, con_kernel=(4, 4), iteration=2)-> np:
    # 灰度
    imgray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # 反色
    imgray = cv2.bitwise_not(imgray)
    # 膨胀
    kernel = np.ones(con_kernel, np.uint8)
    dilation = cv2.dilate(imgray, kernel, iterations=iteration)     #多次迭代，可使非连续区间联通
    # 二值化
    ret, thresh = cv2.threshold(dilation, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # plt.imshow(dilation, cmap='gray')
    # plt.imshow(thresh, cmap='gray')
    # plt.show()

    '''
    最长连续子区间算法
    '''
    horsum, versum = get_image_horizontal_and_vertical_sum(thresh)
    count_x = np.zeros(len(horsum), np.int16)
    count_y = np.zeros(len(versum), np.int16)
    for index, val in enumerate(horsum):    #
        if val != 0:
            count_x[index] = count_x[index - 1] + 1 if index != 0 else 1
    end_x = np.argmax(count_x)
    start_x = end_x - np.max(count_x) + 1

    for index, val in enumerate(versum):
        if val != 0:
            count_y[index] = count_y[index - 1] + 1 if index != 0 else 1
    end_y = np.argmax(count_y)
    start_y = end_y - np.max(count_y) + 1
    return imgray[start_y: end_y, start_x: end_x]

# 矩形化
def square_like_resize(img: np, size=(28, 28)) -> np:
    col, row = img.shape
    if col > row :               # 竖长形
        half_zeros = np.zeros((col, (col-row)//2), np.int8)
        img = np.concatenate((half_zeros, img, half_zeros), axis=1)
    elif col < row:             # 横长形
        half_zeros = np.zeros(((row-col)//2, row), np.int8)
        img = np.concatenate((half_zeros, img, half_zeros), axis=0)
    return cv2.resize(img, size)

if __name__ == '__main__':
    DIR_ZH_TO_ARAB = {'0': '零', '1': '壹', '2': '贰', '3': '叁', '4': '肆', '5': '伍', '6': '陆', '7': '柒',
                       '8': '捌', '9': '玖', '￥': '￥'}
    import os
    for root, dirs, files in os.walk(r'C:\Users\smile\PycharmProjects\pzyq_HeroReco\sql\图片数据库(去黑框)'):
        for file in files:
            file_path = os.path.join(root, file)
            print(file_path)
            # plt.imshow(square_img, cmap='gray')
            # plt.show()
            # import time
            # time.sleep(0.3)

            # 保存（不分类）
            old_root, num_dir = os.path.split(root.replace('去黑框', '标准化'))
            new_root, _class = os.path.split(old_root)

            if _class == '投标价(大写)' or num_dir == '￥':
                # 处理大写字体情况
                img = plt.imread(file_path)
                new_path = os.path.join(new_root, DIR_ZH_TO_ARAB[num_dir])
                main_part_img = get_main_part(img, con_kernel=(10, 10), iteration=2)    # 汉字可能偏旁部首分割距离大
                square_img = square_like_resize(main_part_img, size=(140, 140))         # 汉字部分需要高分辨率

            else:
                img = plt.imread(file_path)
                new_path = os.path.join(new_root, num_dir)
                main_part_img = get_main_part(img)
                square_img = square_like_resize(main_part_img, size=(28, 28))

            # 图片展示
            # plt.imshow(square_img, cmap='gray')
            # plt.show()
            # exit()
            if os.path.exists(new_path) is False:
                os.makedirs(new_path)
            plt.imsave(os.path.join(new_path, file), square_img, cmap='gray')

