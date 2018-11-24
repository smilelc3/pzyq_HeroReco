# author smile
# 实现图片翻转检测

import numpy as np
from matplotlib import pyplot as plt
import cv2
# 矩形边界宽容度
tolerance_size = 60

def is_reverse_detection(img: np)-> bool:
    # 切割左上小块
    flag_img = img[69 - tolerance_size:134 + tolerance_size, 69 - tolerance_size: 134 + tolerance_size]
    # 灰度二值化
    gray = cv2.cvtColor(flag_img, cv2.COLOR_RGB2GRAY)
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # 展示黑点状态
    # plt.imshow(binary, cmap='gray')
    # plt.show()
    black_tot = 0
    for i in range(binary.shape[0]):
        for j in range(binary.shape[1]):
            if binary[i, j] == 0 :
                black_tot += 1
            # print(binary[i, j])
    # print(black_tot)
    if black_tot >= (134 - 65)**2 * 0.73:
        return False
    else:
        return True


if __name__ == '__main__':
    for i in range(1, 273 + 1):
        try:
            img = plt.imread(r'人工填写20181122/%04d.jpg'%i)
            crop_img = cv2.resize(img, (2480, 1748), interpolation=cv2.INTER_CUBIC)
            print(is_reverse_detection(crop_img))
        except FileNotFoundError:
            pass
