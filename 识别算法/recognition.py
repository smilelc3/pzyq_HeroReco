# coding: utf-8

import numpy as np
import cv2
from 分割与矫正.edge_fixedposition_cutting import cutting        # 切割
from 分割与矫正.remove_black_border import scan_line_method      # 扫描线算法去黑框
from 分割与矫正.reverse_recognition import is_reverse_detection  # 反转检测
from 分割与矫正.image_enhancement import get_main_part, square_like_resize # 图像矩形标准化
from matplotlib import pyplot as plt
from keras.models import load_model

class Recognition:
    def __init__(self, original_image: np, num_model_path: str):
        self.image = original_image
        self.is_need_flip = is_reverse_detection(original_image)
        self.remove_border_iteration = 2
        self.NUM_SIZE = (28, 28)
        self.ZH_SIZE = (140, 140)
        self.num_model = load_model(num_model_path)
        self.parts_img = {}         # 存储分割结果
        self.parts_result = {}      # 存储识别结果

    # 获取切割图部分
    def get_parts_img(self):
        parts = {}
        if self.is_need_flip is True:
            parts = cutting(cv2.flip(self.image, -1))
        else:
            parts = cutting(self.image)
        self.parts_img = self._image_enhancement(parts)
        return self.parts_img

    def get_recognition_results(self):
        if self.parts_img == {}:
            print(f'please run {self.__class__}.get_parts_img() first !')

        # 玉石编号
        predict = []
        for gray_img in self.parts_img['stone_num']:
            img_normalized = gray_img / 255
            predict.append(img_normalized)
        img_normalized = np.array(predict)
        img_normalized = img_normalized.reshape(img_normalized.shape[0], self.NUM_SIZE[0], self.NUM_SIZE[1], 1)
        predict = self.num_model.predict_classes(img_normalized)
        self.parts_result['stone_num'] = predict


        # 底标价
        predict = []
        for gray_img in self.parts_img['bottomprice']:
            img_normalized = gray_img / 255
            predict.append(img_normalized)
        img_normalized = np.array(predict)
        img_normalized = img_normalized.reshape(img_normalized.shape[0], self.NUM_SIZE[0], self.NUM_SIZE[1], 1)
        predict = self.num_model.predict_classes(img_normalized)
        self.parts_result['bottomprice'] = predict


        # 投标价小写
        predict = []
        for gray_img in self.parts_img['priceLowercase']:
            img_normalized = gray_img / 255
            predict.append(img_normalized)
        img_normalized = np.array(predict)
        img_normalized = img_normalized.reshape(img_normalized.shape[0], self.NUM_SIZE[0], self.NUM_SIZE[1], 1)
        predict = self.num_model.predict_classes(img_normalized)
        self.parts_result['priceLowercase'] = predict


        # 会员编号
        predict = []
        for gray_img in self.parts_img['Membernum']:
            img_normalized = gray_img / 255
            predict.append(img_normalized)
        img_normalized = np.array(predict)
        img_normalized = img_normalized.reshape(img_normalized.shape[0], self.NUM_SIZE[0], self.NUM_SIZE[1], 1)
        predict = self.num_model.predict_classes(img_normalized)
        self.parts_result['Membernum'] = predict


        # 会员电话号码
        predict = []
        for gray_img in self.parts_img['Memberphone']:
            img_normalized = gray_img / 255
            predict.append(img_normalized)
        img_normalized = np.array(predict)
        img_normalized = img_normalized.reshape(img_normalized.shape[0], self.NUM_SIZE[0], self.NUM_SIZE[1], 1)
        predict = self.num_model.predict_classes(img_normalized)
        self.parts_result['Memberphone'] = predict


        return self.parts_result


    def _image_enhancement(self, ori_parts):
        # TODO 处理 ori_parts['Membername'] 和 ori_parts['priceUppercase']
        # parts 存储标准化后图片
        parts = {}

        # 玉石编号
        parts['stone_num'] = []
        for val in ori_parts['stone_num'][1]:
            val = scan_line_method(val, self.remove_border_iteration)           # 去边框
            main_part_img = get_main_part(val)                                  # 图片增强
            val = square_like_resize(main_part_img, size=self.NUM_SIZE)
            parts['stone_num'].append(val)

        # 底标价
        parts['bottomprice'] = []
        for val in ori_parts['bottomprice'][1]:
            val = scan_line_method(val, self.remove_border_iteration)           # 去边框
            main_part_img = get_main_part(val)                                  # 图片增强
            val = square_like_resize(main_part_img, size=self.NUM_SIZE)
            parts['bottomprice'].append(val)

        # 投标价小写
        parts['priceLowercase'] = []
        for val in ori_parts['priceLowercase'][1]:
            val = scan_line_method(val, self.remove_border_iteration)  # 去边框
            main_part_img = get_main_part(val)  # 图片增强
            val = square_like_resize(main_part_img, size=self.NUM_SIZE)
            parts['priceLowercase'].append(val)

        # 会员编号
        parts['Membernum'] = []
        for val in ori_parts['Membernum'][1]:
            val = scan_line_method(val, self.remove_border_iteration)  # 去边框
            main_part_img = get_main_part(val)  # 图片增强
            val = square_like_resize(main_part_img, size=self.NUM_SIZE)
            parts['Membernum'].append(val)

        # 会员电话号码
        parts['Memberphone'] = []
        for val in ori_parts['Memberphone'][1]:
            val = scan_line_method(val, self.remove_border_iteration)  # 去边框
            main_part_img = get_main_part(val)  # 图片增强
            val = square_like_resize(main_part_img, size=self.NUM_SIZE)
            parts['Memberphone'].append(val)

        return parts


if __name__ == '__main__':
    img_path = r'C:\Users\smile\PycharmProjects\pzyq_HeroReco\sql\人工填写20181122\0003.jpg'
    img = plt.imread(img_path)
    num_model_path = r'C:\Users\smile\PycharmProjects\pzyq_HeroReco\识别算法\阿拉伯数字识别\keras_99_45\model-99-45_add_my.h5'
    recognitionTest = Recognition(img, num_model_path=num_model_path)
    recognitionTest.get_parts_img()
    print(recognitionTest.get_recognition_results())