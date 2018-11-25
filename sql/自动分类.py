from matplotlib import pyplot as plt
from 分割与矫正.reverse_recognition import is_reverse_detection
from 分割与矫正.edge_fixedposition_cutting import cutting, zfcutfixde_show
import cv2
import time

if __name__ == '__main__':
    for i in range(1, 100 + 1):
        try:
            img = plt.imread(r'人工填写20181122/%04d.jpg' % i)
            img_txt = open(r'人工填写20181122/%04d.txt' % i, 'r', encoding='utf-8').readlines()
            crop_img = cutting(img)

            # 处理会员编号
            '''
            vip_num = img_txt[1].strip()
            for index, val in enumerate(vip_num):
                plt.imshow(crop_img['stone_num'][1][index])
                plt.show()
                print('val:', val)
                flag = input()
                if flag == '' or '\n':      # 无问题
                    file_name = '图片数据库/会员编号/' + val + '/' + str(int(time.time() * 10)) + '.jpg'
                    print(file_name)
                    plt.imsave(file_name, crop_img['stone_num'][1][index])
                elif flag != -1:
                    file_name = '图片数据库/会员编号/' + flag + '/' + str(int(time.time() * 10)) + '.jpg'
                    print(file_name)
                    plt.imsave(file_name, crop_img['stone_num'][1][index])
            '''
            # 处理底标价
            vip_num = img_txt[2].strip()
            for index, val in enumerate(vip_num):
                #plt.imshow(crop_img['stone_num'][1][index])
                #plt.show()
                print('val:', val)
                try:
                    file_name = '图片数据库/底标价/' + val + '/' + str(int(time.time() * 1000)) + '.jpg'
                    print(file_name)
                    plt.imsave(file_name, crop_img['bottomprice'][1][index])
                except:
                    print('ERROR:', r'人工填写20181122/%04d.txt' % i)

        except FileNotFoundError:
            pass
