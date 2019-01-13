#coding:utf-8
import tkinter
import cv2
from tkinter.constants import *
from tkinter import ttk
from PIL import Image,ImageTk
from SqlExecute import BidSheetIdentificationCollectfield

def sendStr():
    print('Data Send Ok!')

#  实例化TK类，主窗口必须为.TK(),而其他子窗口为.Toplevel()
top = tkinter.Tk()

# 设置窗口的尺寸大小
#root.geometry(width, height, (screenwidth - width)/2, (screenheight - height)/2)
top.wm_geometry('1200x600+70+20')
# 不允许 改变 窗口的宽和高
top.wm_resizable(False,False)
# 设置窗口标题
top.title('scanner')

menubar = tkinter.Menu(top)
filemenu = tkinter.Menu(menubar, tearoff=0)
#
menubar.add_cascade(label='文件', menu=filemenu)
filemenu.add_command(label='新建')
filemenu.add_command(label='打开')
filemenu.add_command(label='保存')
#
helpmenu = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label='配置', menu=helpmenu)
helpmenu.add_command(label='图片参数')
helpmenu.add_command(label='扫描仪参数')
#
testmenu = tkinter.Menu(menubar,tearoff=0)
menubar.add_checkbutton(label='开始扫描' )

top.config(menu=menubar)

# 设置label标签
#L1 = tkinter.Label(top, text='TCP Sever：\n20108/09/15',width=15, justify=LEFT, relief=RIDGE, background='#6699ff', )\
 #    .pack_configure(anchor=N, side=TOP, ipady=2, pady=2, fill=NONE)
 #搜索框
#frame4 = tkinter.Frame(top,height=4,width=50, relief=RIDGE,bg='#ffffff',bd=5,borderwidth=4)
#frame4.pack(fill=NONE, padx=0,pady=0,side=LEFT,expand=Y, anchor=NW)
#txt2 = tkinter.Text(frame4, height =3, width =10).pack(padx=0, pady=0,side=TOP, anchor=N, expand=0)
#button1 = tkinter.Button(frame4,text='搜索', command=sendStr,bg='#87CEEB').pack(side=LEFT, anchor=NW, padx=2, pady=4)

# 列表
tree = ttk.Treeview(top)
tree.pack(fill=Y, padx=0,pady=0,side=LEFT,expand=Y,anchor=W)

# 定义列
tree["columns"] = ("姓名","年龄","身高","体重")
# 设置列，列还不显示
tree.column("姓名", width=10)
tree.column("年龄", width=10)
tree.column("身高", width=10)
tree.column("体重", width=10)
# 设置表头
tree.heading("姓名", text="姓名-name")
tree.heading("年龄", text="年龄-age")
tree.heading("身高", text="身高-height")
tree.heading("体重", text="体重-weight")
# 添加数据
tree.insert("", 0, text="line1", values=("小郑","34","177cm","70kg"))
tree.insert("", 1, text="line2", values=("小张","43","188cm","90kg"))

# 设置图片显示容器
L2 = tkinter.Label(top, text='扫描图片:',font=('楷体',14),bg='#87CEEB')
L2.pack(fill=NONE, expand=0, side=TOP, anchor=W, padx=0,pady=2)
frame1 = tkinter.Frame(top,height=310,width=50,relief=RIDGE, bg='#dcdcdc',bd=5,borderwidth=4)
frame1.pack(fill=NONE,ipady=2,expand=1,side=TOP, anchor=N)
img = Image.open('C:\\Users\\admin\\Desktop\\项目\\2.jpg')
img1 = img.resize((600, 300),Image.ANTIALIAS)
img_png = ImageTk.PhotoImage(img1)
L3 = tkinter.Label(frame1,height=300,width=600,image = img_png)\
    .pack(fill=NONE, expand=1, side=TOP, anchor=N, padx=2,pady=0,ipadx=170)

# 设置图片信息容器
L3 = tkinter.Label(top, text='图片信息:',font=('楷体',14),bg='#87CEEB')
L3.pack(fill=NONE, expand=0, side=TOP, anchor=W, padx=0,pady=0)
frame3 = tkinter.Frame(top,height=20,width=500,relief=RIDGE, bg='#dcdcdc',bd=5,borderwidth=0)
frame3.pack(fill=X,ipady=0,expand=0)
button1 = tkinter.Button(frame3,text='玉石编号',font=('楷体',13), command=sendStr,bg='#87CEEB').pack(side=LEFT, anchor=N, padx=13, pady=6)
txt1 = tkinter.Text(frame3, height =2.4, width =48).pack(side=LEFT, anchor=N, expand=0, padx=10,pady=6)
txt2 = tkinter.Text(frame3, height =2.4, width =48).pack(side=RIGHT, anchor=N, expand=0,padx=10, pady=6)
button2 = tkinter.Button(frame3,text='底标价',font=('楷体',13), command=sendStr,bg='#87CEEB').pack(side=RIGHT, anchor=N, padx=10, pady=6)

L4 = tkinter.Label(top, text='投标价:', font=('楷体', 14), bg='#87CEEB')
L4.pack(fill=NONE, expand=0, side=TOP, anchor=W, padx=0, pady=0)
frame4 = tkinter.Frame(top,height=20,width=500,relief=RIDGE, bg='#dcdcdc',bd=5,borderwidth=0)
frame4.pack(fill=X,ipady=0,expand=0)
button3 = tkinter.Button(frame4,text='投标价（小写）',font=('楷体',13), command=sendStr,bg='#87CEEB').pack(side=LEFT, anchor=N, padx=10, pady=6)
txt3 = tkinter.Text(frame4, height =2, width =40).pack(side=LEFT, anchor=N, expand=0, padx=10, pady=6)
txt8 = tkinter.Text(frame4, height =2, width =40).pack(side=RIGHT, anchor=N, expand=0, padx=10, pady=6)
button4 = tkinter.Button(frame4,text='投标价（大写）',font=('楷体',13), command=sendStr,bg='#87CEEB').pack(side=RIGHT, anchor=N, padx=10, pady=6)

L5 = tkinter.Label(top, text='投标人:', font=('楷体', 14), bg='#87CEEB')
L5.pack(fill=NONE, expand=0, side=TOP, anchor=W, padx=0, pady=6)
frame5 = tkinter.Frame(top,height=20,width=500,relief=RIDGE, bg='#dcdcdc',bd=5,borderwidth=0)
frame5.pack(fill=X,ipady=0,expand=0,pady=0)
button5 = tkinter.Button(frame5,text='会员号码',font=('楷体',13), command=sendStr,bg='#87CEEB').pack(side=LEFT, anchor=N, padx=14, pady=2)
txt4 = tkinter.Text(frame5, height =2, width =45).pack(side=LEFT, anchor=N, expand=0, padx=12,pady=2)
txt5 = tkinter.Text(frame5, height =2, width =45).pack(side=RIGHT, anchor=N, expand=0, padx=12,pady=2)
button6 = tkinter.Button(frame5,text='联系电话',font=('楷体',13), command=sendStr,bg='#87CEEB').pack(side=RIGHT, anchor=N, padx=14, pady=2)

frame6 = tkinter.Frame(top,height=20,width=500,relief=RIDGE, bg='#dcdcdc',bd=5,borderwidth=0)
frame6.pack(fill=X,ipady=0,expand=0)
button7 = tkinter.Button(frame6,text='姓名',font=('楷体',13), command=sendStr,bg='#87CEEB').pack(side=LEFT, anchor=N, padx=35, pady=6)
txt6 = tkinter.Text(frame6, height =2, width =43).pack(side=LEFT, anchor=N, expand=0,padx=12, pady=6)
txt7 = tkinter.Text(frame6, height =2, width =48).pack(side=RIGHT, anchor=N, expand=0,padx=12, pady=6)
button8 = tkinter.Button(frame6,text='备注',font=('楷体',13), command=sendStr,bg='#87CEEB').pack(side=RIGHT, anchor=N, padx=12, pady=6)

top.mainloop()
# 设置容器2
#frame2 = tkinter.Frame(top, relief=RIDGE,bg='#3366ff')
#frame2.pack(fill=X, padx=2,pady=10,side=TOP)
# 加一个复选框，一个按键
#chk_text = 'Hex Display'
#int_if_choise = tkinter.IntVar()
#chk1 = tkinter.Checkbutton(frame2,text=chk_text,font=('黑体',12),variable=int_if_choise,onvalue='OK',offvalue='NO')
#chk1.pack(fill=NONE,side=LEFT,padx=2,pady=10)
#print('shuchu:',int_if_choise)