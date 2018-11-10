# 定义pipe中类结构
import numpy
import time

class PipeImg:
    def __init__(self, cv2Img:numpy):
        self.np_img = cv2Img                   # numpy初始化
        self.shape = cv2Img.shape           # 图片尺寸数据
        self.create_time = time.time()       # 记录入pipe时间
        self.is_ident = False                # 记录是否能够识别
        self.num = -1,
        self.bottom_price = 0
        self.tender_price = 0
        self.tender_price_zh = 0
        self.vip_num = -1
        self.phone_num = -1
        self.vip_name = -1
        self.remark = ''

    def set_tender_data(self,
                        num:str,                # 玉石编号
                        bottom_price:int,       # 地标价
                        tender_price:int,       # 投标价（小写）
                        tender_price_zh:list,   # 投标价（大写）
                        vip_num:int,            # 会员号码
                        phone_num:int,          # 联系电话
                        vip_name:list,          # 姓名
                        remark:str              # 备注
                        ):
        self.num = num,
        self.bottom_price = bottom_price
        self.tender_price = tender_price
        self.tender_price_zh = tender_price_zh
        self.vip_num = vip_num
        self.phone_num = phone_num
        self.vip_name = vip_name
        self.remark =remark


    def get_tender_data(self)->list:
        try:
            self.is_ident = True
            return [self.num, self.bottom_price, self.tender_price,
                    self.tender_price_zh, self.vip_name, self.phone_num,
                    self.vip_name, self.remark]
        # TODO 错误处理机制
        except AttributeError:
            print('无法识别该扫描单')