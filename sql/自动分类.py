from matplotlib import pyplot as plt
from 分割与矫正.reverse_recognition import is_reverse_detection
from 分割与矫正.edge_fixedposition_cutting import cutting, zfcutfixded_show
import cv2
import time

if __name__ == '__main__':
    for i in range(1, 293 + 1):
        try:
            img = plt.imread(r'人工填写20181126/%04d.jpg' % i)
            print(r'人工填写20181126/%04d.jpg' % i)
            img_txt = open(r'人工填写20181126/%04d.txt' % i, 'r', encoding='utf-8').readlines()
            crop_img = cutting(img)

            # 处理会员编号
            vip_num = img_txt[1].strip()
            for index, val in enumerate(vip_num):
                #plt.imshow(crop_img['stone_num'][1][index])
                #plt.show()
                print('val:', val)
                try:
                    file_name = '图片数据库(原始)/玉石编号/' + val + '/' + str(int(time.time() * 1000)) + '.jpg'
                    print(file_name)
                    plt.imsave(file_name, crop_img['stone_num'][1][index])
                except:
                    print('ERROR:', r'人工填写20181126/%04d.txt' % i)


            # 处理底标价
            vip_num = img_txt[2].strip()
            for index, val in enumerate(vip_num):
                #plt.imshow(crop_img['stone_num'][1][index])
                #plt.show()
                print('val:', val)
                try:
                    file_name = '图片数据库(原始)/底标价/' + val + '/' + str(int(time.time() * 1000)) + '.jpg'
                    print(file_name)
                    plt.imsave(file_name, crop_img['bottomprice'][1][index])
                except:
                    print('ERROR:', r'人工填写20181126/%04d.txt' % i)

            # 处理投标价（小写）
            vip_num = img_txt[3].strip()
            for index, val in enumerate(vip_num):
                #plt.imshow(crop_img['stone_num'][1][index])
                #plt.show()
                print('val:', val)
                try:
                    file_name = '图片数据库(原始)/投标价(小写)/' + val + '/' + str(int(time.time() * 1000)) + '.jpg'
                    print(file_name)
                    plt.imsave(file_name, crop_img['priceLowercase'][1][index])
                except:
                    print('ERROR:', r'人工填写20181126/%04d.txt' % i)

            # 处理投标价（大写）
            vip_num = img_txt[3].strip()
            for index, val in enumerate(vip_num):
                #plt.imshow(crop_img['stone_num'][1][index])
                #plt.show()
                print('val:', val)
                try:
                    file_name = '图片数据库(原始)/投标价(大写)/' + val + '/' + str(int(time.time() * 1000)) + '.jpg'
                    print(file_name)
                    plt.imsave(file_name, crop_img['priceUppercase'][1][index])
                except:
                    print('ERROR:', r'人工填写20181126/%04d.txt' % i)

            # 处理会员号码
            vip_num = img_txt[4].strip()
            for index, val in enumerate(vip_num):
                #plt.imshow(crop_img['stone_num'][1][index])
                #plt.show()
                print('val:', val)
                try:
                    file_name = '图片数据库(原始)/会员编号/' + val + '/' + str(int(time.time() * 1000)) + '.jpg'
                    print(file_name)
                    plt.imsave(file_name, crop_img['Membernum'][1][index])
                except:
                    print('ERROR:', r'人工填写20181126/%04d.txt' % i)
            
            # 处理电话
            vip_num = img_txt[5].strip()
            for index, val in enumerate(vip_num):
                #plt.imshow(crop_img['stone_num'][1][index])
                #plt.show()
                print('val:', val)
                try:
                    file_name = '图片数据库(原始)/电话/' + val + '/' + str(int(time.time() * 1000)) + '.jpg'
                    print(file_name)
                    plt.imsave(file_name, crop_img['Memberphone'][1][index])
                except:
                    print('ERROR:', r'人工填写20181126/%04d.txt' % i)

        except FileNotFoundError:
            pass
