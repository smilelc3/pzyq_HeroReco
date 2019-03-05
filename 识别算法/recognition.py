# coding: utf-8

import numpy as np
import cv2
import json
from 分割与矫正.edge_fixedposition_cutting import cutting        # 切割
from 分割与矫正.remove_black_border import scan_line_method      # 扫描线算法去黑框
from 分割与矫正.reverse_recognition import is_reverse_detection  # 反转检测
from 分割与矫正.image_enhancement import get_main_part, square_like_resize # 图像矩形标准化
from matplotlib import pyplot as plt
from keras.models import load_model

class Recognition:
    def __init__(self, num_model_path: str, zh_num_model_path: str, HCCR_model_path: str, label_zh_to_json_path: str):
        self.is_need_flip = False
        self.remove_border_iteration = 2
        self.NUM_SIZE = (28, 28)
        self.ZH_NUM_SIZE = (140, 140)
        self.HCCR_SIZE = (96, 96)
        self.num_model = load_model(num_model_path)
        self.zh_num_model = load_model(zh_num_model_path)
        self.zh_upper_num = ['￥', '零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']         # 大学数字识别转换
        self.HCCR_model = load_model(HCCR_model_path)
        self.HCCR_dict = json.loads(open(label_zh_to_json_path, 'r', encoding='utf-8').read())
        self.parts_img = {}         # 存储分割结果
        self.parts_result = {}      # 存储识别结果

    # 获取切割图部分
    def get_parts_img(self, original_image: np):
        self.image = original_image
        self.is_need_flip = is_reverse_detection(original_image)
        parts = {}
        # 反转检测
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

        # 投标价大写
        predict = []
        for gray_img in self.parts_img['priceUppercase']:
            img_normalized = gray_img / 255
            predict.append(img_normalized)
        img_normalized = np.array(predict)
        img_normalized = img_normalized.reshape(img_normalized.shape[0], self.ZH_NUM_SIZE[0], self.ZH_NUM_SIZE[1], 1)
        predict = self.zh_num_model.predict_classes(img_normalized)
        self.parts_result['priceUppercase'] = [self.zh_upper_num[val] for val in predict]

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

        # 会员姓名
        predict = []
        for gray_img in self.parts_img['Membername']:
            img_normalized = gray_img / 255
            predict.append(img_normalized)
        img_normalized = np.array(predict)
        img_normalized = img_normalized.reshape(img_normalized.shape[0], self.HCCR_SIZE[0], self.HCCR_SIZE[1], 1)
        predict = self.HCCR_model.predict_classes(img_normalized)
        self.parts_result['Membername'] = [self.HCCR_dict[str(val)] for val in predict]

        return self.parts_result


    def _image_enhancement(self, ori_parts):
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

        # 投标价大写
        parts['priceUppercase'] = []
        for val in ori_parts['priceUppercase'][1]:
            val = scan_line_method(val, self.remove_border_iteration)  # 去边框
            main_part_img = get_main_part(val, con_kernel=(10, 10), iteration=2)  # 图片增强
            val = square_like_resize(main_part_img, size=self.ZH_NUM_SIZE)  # 方格化
            parts['priceUppercase'].append(val)

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

        # 会员姓名
        parts['Membername'] = []
        for val in ori_parts['Membername'][1]:
            val = scan_line_method(val, self.remove_border_iteration)  # 去边框
            main_part_img = get_main_part(val, con_kernel=(10, 10), iteration=2)  # 图片增强
            val = square_like_resize(main_part_img, size=self.HCCR_SIZE)
            parts['Membername'].append(val)
        return parts


if __name__ == '__main__':
    img_path = r'C:\Users\smile\PycharmProjects\pzyq_HeroReco\sql\人工填写20181122\0003.jpg'
    img = plt.imread(img_path)

    # 阿拉伯数字模型
    num_model_path = r'model-99-45_add_my.h5'
    # 大写数字识别模型
    zh_num_model_path = r'model_HWDB_change.h5'
    # 汉字识别模型
    HCCR_model_path = r'model_HCCR_CNN9Layer.hdf5'
    # 汉字识别对应表
    label_zh_to_json_path = r'label_to_zh.json'

    recognitionTest = Recognition(
        num_model_path=num_model_path,
        zh_num_model_path=zh_num_model_path,
        HCCR_model_path=HCCR_model_path,
        label_zh_to_json_path=label_zh_to_json_path,
    )
    recognitionTest.get_parts_img(img)
    plt.subplot(1, 4, 1)
    plt.imshow(recognitionTest.parts_img['Membername'][0], cmap='gray')
    plt.subplot(1, 4, 2)
    plt.imshow(recognitionTest.parts_img['Membername'][1], cmap='gray')
    plt.subplot(1, 4, 3)
    plt.imshow(recognitionTest.parts_img['Membername'][2], cmap='gray')
    plt.subplot(1, 4, 4)
    plt.imshow(recognitionTest.parts_img['Membername'][3], cmap='gray')
    print(recognitionTest.get_recognition_results())
    plt.show()