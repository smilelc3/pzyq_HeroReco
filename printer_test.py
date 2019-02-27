import win32com.client
import win32gui
import time
t1 = 0

class EventHandler:
        def OnBeforeScan(self):
            global t1
            t1 = time.clock()
            print("beforescan", )

        def OnPageDoneDib(self,dib,resolution):
            global count,devent, t1
            count=count+1
            devent.SaveJpgFile("C:\\Users\\402\\Desktop\\roolar1014\\"+str(count)+".jpg", dib, resolution, 85)
            print("C:\\Users\\402\\Desktop\\roolar1014\\"+str(count)+".jpg", end='')

            # 1 to show img
            # cv2.nameWindow("scanner")
            # img = cv2.imread("C:\\Users\\402\\Desktop\\roolar1014\\" + str(count) + ".jpg")
            # cv2.imshow("scanner", img)
            # cv2.imshow("scanner", dib)

            t2 = time.clock()
            print(" time:{:2.1f}, dib:{}".format(t2 - t1, dib))
            t1 = t2

            # 2 to send to recongnize pipe



        def OnPageDone(self):
            win32gui.PostQuitMessage(0)


count = 0
devent = win32com.client.DispatchWithEvents('TechHeroScanProj1.TechHeroScan',EventHandler)
# devent.SelectScanner()
# devent.ShowSetupBeforeScan = True
devent.Pixel_Type = 2                # 扫描彩色
devent.Duplex = False                # 单面
devent.Resolution = 300              # 分辨率
devent.Brightness = 9                # 亮度    bri = target * 2000/255 - 1000
devent.Contrast = -1000              # 对比度  con = target * 2000/7 - 1000
devent.PaperSize = -1                # 纸张大小：自动判断纸张大小
devent.ShowIndicators = False        # 扫描是否显示进度
# devent.AutoFeed = True
devent.ScanToDib(0)
devent.SetAutoDeskew(True)

import pythoncom
pythoncom.PumpMessages()
# create a pipe and a process

# in another process multiprocess
    # 1 GUI

    # 2 get img from pipe

    # 3 cv2.imshow()

    # 4 write the recognized results to mysql

