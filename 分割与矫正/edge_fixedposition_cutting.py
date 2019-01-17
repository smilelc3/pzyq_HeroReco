# @author:zdd

import cv2
import numpy as np
from matplotlib import pyplot as plt
from 分割与矫正.reverse_recognition import is_reverse_detection
# 主体框分割算法
def cutting(img:np):
    # 获取图片
    """
        其中各参数所表达的意义：
        src：原图像；
        d：像素的邻域直径，可有sigmaColor和sigmaSpace计算可得；
        sigmaColor：颜色空间的标准方差，一般尽可能大；
        sigmaSpace：坐标空间的标准方差(像素单位)，一般尽可能小。
    """
    if is_reverse_detection(img):
        img = cv2.flip(img, -1)     # 水平垂直翻转
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (9, 9), 0)  # 高斯去噪(会出现上边部分缺失)
    # blurred = cv2.bilateralFilter(src=gray, d=0, sigmaColor=100, sigmaSpace=15)  # 高斯双边滤波(会出现只有条形码)
    # blurred = cv2.medianBlur(gray, 5)#与高斯滤波效果类似

    # 索比尔算子来计算x、y方向梯度
    gradX = cv2.Sobel(blurred, ddepth=cv2.CV_32F, dx=1, dy=0)
    gradY = cv2.Sobel(blurred, ddepth=cv2.CV_32F, dx=0, dy=1)

    gradient = cv2.subtract(gradX, gradY)  # 图像矩阵相加
    # gradient = cv2.addWeighted(gradX,5,gradY,1,6)#图像叠加or图像混合加权实现
    gradient = cv2.convertScaleAbs(gradient)  # 将其转回原来的uint8形式
    blurred = cv2.GaussianBlur(gradient, (9, 9), 0)
    (_, thresh) = cv2.threshold(blurred, 90, 255, cv2.THRESH_BINARY)  # 用于获取二元值的灰度图像
    # 建立一个椭圆核函数
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))  # OpenCV定义的结构元素
    # 执行图像形态学, 细节直接查文档，很简单
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)  # 闭运算
    # 先膨胀后腐蚀的操作称之为闭操作。它具有填充物体内细小空洞，连接邻近物体和平滑边界的作用
    # 先腐蚀后膨胀的操作称之为开操作。它具有消除细小物体，在纤细处分离物体和平滑较大物体边界的作用。
    closed = cv2.erode(closed, None, iterations=4)  # 腐蚀图像
    closed = cv2.dilate(closed, None, iterations=1)  # 膨胀图像

    # 这里opencv3返回的是三个参数
    (_, cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)  # 寻找轮廓
    c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
    # compute the rotated bounding box of the largest contour
    rect = cv2.minAreaRect(c)  # 返回点集cnt的最小外接矩形
    box = np.int0(cv2.boxPoints(rect))  # 找到定位标记的矩形包围盒
    # 因为这个函数有极强的破坏性，所有需要在img.copy()上画
    # draw a bounding box arounded the detected barcode and display the image
    # draw_img = cv2.drawContours(img.copy(), [box], -1, (0, 0, 255), 3)

    main_img = perspective_vertical_correction(img, box)

    # 进行一次尺寸变换，ppi=300
    result_img = Fixedpoint_cutting(main_img)
    return result_img

# 透视变换+垂直矫正+切割
def perspective_vertical_correction(img, box: list) -> np:
    from operator import itemgetter
    # box可能乱序，需要重新排序
    meanX = np.mean([p[0] for p in box])
    meanY = np.mean([p[1] for p in box])
    # print(box, meanX, meanY)
    for point in box:
        if point[0] < meanX and point[1] < meanY:
            x1, y1 = point
        if point[0] > meanX and point[1] < meanY:
            x2, y2 = point
        if point[0] < meanX and point[1] > meanY:
            x3, y3 = point
        if point[0] > meanX and point[1] > meanY:
            x4, y4 = point

    # 生成透视变换矩阵，需要两个对应矩阵
    pts1 = np.float32([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])  # 原图四个像素点
    # print([x1, y1], [x2, y2], [x3, y3], [x4, y4])
    pts2 = np.float32([[66, 388], [2415, 388], [66, 1677], [2415, 1677]])  # 变换后分别在左上、右上、左下、右下四个点
    # 进行透视变换
    M = cv2.getPerspectiveTransform(pts1, pts2)
    dst = cv2.warpPerspective(img, M, (2480, 1748))
    # plt.imshow(dst)
    # plt.show()
    return dst[388: 1677, 66: 2415]

# 按像素点切割
def Fixedpoint_cutting(img: np) -> dict:
    tailorpic = cv2.resize(img, (2349,1289), interpolation=cv2.INTER_CUBIC)
    # 玉石编号
    region_yushi = tailorpic[3:207, 516:1177]
    dx = (1177-516)/5
    imgstone = region_yushi[0:204, 0:int(dx)],region_yushi[0:204, int(dx):int(dx*2)],region_yushi[0:204, int(dx*2):int(dx*3)],region_yushi[0:204, int(dx*3):int(dx*4)],region_yushi[0:204, int(dx*4):int(dx*5)]
    # 玉石底价
    region_pricebottom = tailorpic[88:207, 1518:2346]
    dx = (2346-1518) / 8
    imgbottom_price = region_pricebottom[0:119, 0:int(dx)], region_pricebottom[0:119, int(dx):int(dx*2)], region_pricebottom[0:119, int(dx*2):int(dx*3)], region_pricebottom[0:119, int(dx*3):int(dx*4)], region_pricebottom[0:119, int(dx*4):int(dx*5)], region_pricebottom[0:119, int(dx*5):int(dx*6)], region_pricebottom[0:119, int(dx*6):int(dx*7)], region_pricebottom[0:119, int(dx*7):int(dx*8)]
    # 小写报价
    region_priceLeast = tailorpic[282:378, 624:2346]
    dx = (2346-624) / 8
    imgbid_prices_Lowercase = region_priceLeast[0:378-282, 0:int(dx)], region_priceLeast[0:378-282, int(dx):int(dx*2)], region_priceLeast[0:378-282, int(dx*2):int(dx*3)], region_priceLeast[0:378-282, int(dx*3):int(dx*4)], region_priceLeast[0:378-282, int(dx*4):int(dx*5)], region_priceLeast[0:378-282, int(dx*5):int(dx*6)], region_priceLeast[0:378-282, int(dx*6):int(dx*7)], region_priceLeast[0:378-282, int(dx*7):int(dx*8)]
    # 大写报价
    region_priceMost = tailorpic[373:563, 624:2346]
    dx = (2346-624) / 8
    imgbid_prices_Uppercase = region_priceMost[0:563-373, 0:int(dx)], region_priceMost[0:563-373, int(dx):int(dx*2)], region_priceMost[0:563-373, int(dx*2):int(dx*3)], region_priceMost[0:563-373, int(dx*3):int(dx*4)], region_priceMost[0:563-373, int(dx*4):int(dx*5)], region_priceMost[0:563-373, int(dx*5):int(dx*6)], region_priceMost[0:563-373, int(dx*6):int(dx*7)], region_priceMost[0:563-373, int(dx*7):int(dx*8)]
    # 会员号码
    region_Membersnum = tailorpic[558:729, 693:1177]
    dx = (1177-693)/5
    imgMember_num = region_Membersnum[0:729-558, 0:int(dx)], region_Membersnum[0:729-558, int(dx):int(dx*2)], region_Membersnum[0:729-558, int(dx*2):int(dx*3)], region_Membersnum[0:729-558, int(dx*3):int(dx*4)], region_Membersnum[0:729-558, int(dx*4):int(dx*5)]
    # 会员姓名
    region_Membersname = tailorpic[724:899, 632:1177]
    dx = (1177-632)/4
    imgMembers_name = region_Membersname[0:899-724, 0:int(dx)], region_Membersname[0:899-724, int(dx):int(dx*2)], region_Membersname[0:899-724, int(dx*2):int(dx*3)], region_Membersname[0:899-724, int(dx*3):int(dx*4)]
    # 会员电话
    region_Membersphone = tailorpic[558:729, 1541:2346]
    dx = (2346-1541)/11
    imgMember_phone = region_Membersphone[0:729-558, 0:int(dx)], region_Membersphone[0:729-558, int(dx):int(dx*2)], region_Membersphone[0:729-558, int(dx*2):int(dx*3)], region_Membersphone[0:729-558, int(dx*3):int(dx*4)], region_Membersphone[0:729-558, int(dx*4):int(dx*5)], region_Membersphone[0:729-558, int(dx*5):int(dx*6)], region_Membersphone[0:729-558, int(dx*6):int(dx*7)], region_Membersphone[0:729-558, int(dx*7):int(dx*8)], region_Membersphone[0:729-558, int(dx*8):int(dx*9)], region_Membersphone[0:729-558, int(dx*9):int(dx*10)], region_Membersphone[0:729-558, int(dx*10):int(dx*11)]

    # 返回字典
    saveimg = {
        'stone_num': (region_yushi, imgstone),
        'bottomprice': (region_pricebottom, imgbottom_price),
        'priceLowercase': (region_priceLeast, imgbid_prices_Lowercase),
        'priceUppercase': (region_priceMost, imgbid_prices_Uppercase),
        'Membernum': (region_Membersnum, imgMember_num),
        'Membername': (region_Membersname, imgMembers_name),
        'Memberphone': (region_Membersphone, imgMember_phone)
    }
    return saveimg


# 主要用以绘图展示
def zfcutfixde_show(result_img: np):
    stone_num = result_img['stone_num']
    bottomprice = result_img['bottomprice']
    bid_prices_Lowercase =  result_img['priceLowercase']
    bid_prices_Uppercase = result_img['priceUppercase']
    Members_num = result_img['Membernum']
    Members_name = result_img['Membername']
    Members_phone = result_img['Memberphone']

    plt.subplot(421)
    plt.imshow(stone_num[1][0])
    plt.subplot(422)
    plt.imshow(bottomprice[1][2])
    plt.subplot(423)
    plt.imshow(bid_prices_Lowercase[1][4])
    plt.subplot(424)
    plt.imshow(bid_prices_Uppercase[1][2])
    plt.subplot(425)
    plt.imshow(Members_num[1][4])
    plt.subplot(426)
    plt.imshow(Members_phone[1][3])
    plt.subplot(427)
    plt.imshow(Members_name[1][3])
    plt.show()


if __name__ == '__main__':
    img = plt.imread(r'0001.jpg')
    crop_img = cutting(img)

    zfcutfixde_show(crop_img)



