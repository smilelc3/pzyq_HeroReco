import tkinter
from tkinter.constants import *
from tkinter import ttk
from PIL import Image,ImageTk
from 识别算法.recognition import Recognition

#from matplotlib import pyplot as plt
#from SqlExecute import BidSheetIdentificationCollectfield

def sendStr():
    print('Data Send Ok!')

#  实例化TK类，主窗口必须为.TK(),而其他子窗口为.Toplevel()
top = tkinter.Tk()

# 设置窗口的尺寸大小
#root.geometry(width, height, (screenwidth - width)/2, (screenheight - height)/2)
top.wm_geometry('1000x650')
# 不允许 改变 窗口的宽和高
top.wm_resizable(False,False)
# 设置窗口标题
top.title('scanner')

num_model_path = r'C:\Users\李若澜\Desktop\项目\model-99-45_add_my.h5'
recognitionTest = Recognition(num_model_path=num_model_path)

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
frame = tkinter.Frame(top,height=4,width=50, relief=RIDGE,bg='#ffffff',bd=5,borderwidth=4)
frame.pack(fill=NONE, padx=0,pady=0,side=TOP,expand=Y, anchor=NW)
txt = tkinter.Text(frame, height =3, width =10).pack(padx=0, pady=0,side=TOP, anchor=N, expand=0)
button1 = tkinter.Button(frame,text='搜索', command=sendStr,bg='#87CEEB').pack(side=LEFT, anchor=NW, padx=2, pady=4)

# 列表
tree = ttk.Treeview(top)
tree.pack(fill=Y, padx=0,pady=0,side=LEFT,expand=Y,anchor=W)

columns = ("姓名", "IP地址")
treeview = ttk.Treeview(tree, height=18, show="headings", columns=columns)  # 表格

treeview.column("姓名", width=150, anchor='center')  # 表示列,不显示
treeview.column("IP地址", width=150, anchor='center')

treeview.heading("姓名", text="姓名")  # 显示表头
treeview.heading("IP地址", text="IP地址")

treeview.pack(side=LEFT, fill=BOTH)

name = ['电脑1', '服务器', '笔记本']
ipcode = ['10.13.71.223', '10.25.61.186', '10.25.11.163']
for i in range(min(len(name), len(ipcode))):  # 写入数据
    treeview.insert('', i, values=(name[i], ipcode[i]))

# 设置图片显示容器
ScanPicture = tkinter.Label(top, text='扫描图片:',font=('楷体',16))
ScanPicture.pack(fill=NONE, expand=0, side=TOP, anchor=W, padx=0,pady=2)
frame1 = tkinter.Frame(top,height=600,width=50,relief=RIDGE, bg='#dcdcdc',bd=5,borderwidth=4)
frame1.pack(fill=NONE,ipady=2,expand=1,side=TOP, anchor=N)
img = Image.open('C:\\Users\\李若澜\\Desktop\\项目\\1.jpg')
img1 = img.resize((600, 400),Image.ANTIALIAS)
img_png = ImageTk.PhotoImage(img1)
StoneMessage = tkinter.Label(frame1,height=300,width=500,image = img_png)\
    .pack(fill=NONE, expand=1, side=TOP, anchor=N, padx=2,pady=0,ipadx=170)

# 设置图片信息容器
StoneMessage = tkinter.Label(top, text='玉石信息:',font=('楷体',16))
StoneMessage.pack(fill=NONE, expand=0, side=TOP, anchor=W, padx=0,pady=0)
frame3 = tkinter.Frame(top,height=20,width=500,relief=RIDGE, bg='#dcdcdc',bd=5,borderwidth=0)
frame3.pack(fill=X,ipady=0,expand=0)
button1 = tkinter.Label(frame3,text='玉石编号',font=('楷体',16),bg='#dcdcdc').pack(side=LEFT, anchor=N, pady=6)
txt1 = tkinter.Text(frame3, height =2, width =4)
txt1.pack(side=LEFT, anchor=N, expand=0,pady=6)
txt2 = tkinter.Text(frame3, height =2, width =4)
txt2.pack(side=LEFT, anchor=N, expand=0,pady=6)
txt3 = tkinter.Text(frame3, height =2, width =4)
txt3.pack(side=LEFT, anchor=N, expand=0, pady=6)
txt4 = tkinter.Text(frame3, height =2, width =4)
txt4.pack(side=LEFT, anchor=N, expand=0, pady=6)
txt5 = tkinter.Text(frame3, height =2, width =4)
txt5.pack(side=LEFT, anchor=N, expand=0, pady=6)

txt6 = tkinter.Text(frame3, height =2, width =4)
txt6.pack(side=RIGHT, anchor=N, expand=0, pady=6)
txt7 = tkinter.Text(frame3, height =2, width =4)
txt7.pack(side=RIGHT, anchor=N, expand=0, pady=6)
txt8 = tkinter.Text(frame3, height =2, width =4)
txt8.pack(side=RIGHT, anchor=N, expand=0, pady=6)
txt9 = tkinter.Text(frame3, height =2, width =4)
txt9.pack(side=RIGHT, anchor=N, expand=0, pady=6)
txt10 = tkinter.Text(frame3, height =2, width =4)
txt10.pack(side=RIGHT, anchor=N, expand=0, pady=6)
txt11= tkinter.Text(frame3, height =2, width =4)
txt11.pack(side=RIGHT, anchor=N, expand=0, pady=6)
txt12= tkinter.Text(frame3, height =2, width =4)
txt12.pack(side=RIGHT, anchor=N, expand=0, pady=6)
txt13= tkinter.Text(frame3, height =2, width =4)
txt13.pack(side=RIGHT, anchor=N, expand=0, pady=6)
txt14= tkinter.Text(frame3, height =2, width =4)
txt14.pack(side=RIGHT, anchor=N, expand=0, pady=6)
txt15= tkinter.Text(frame3, height =2, width =4)
txt15.pack(side=RIGHT, anchor=N, expand=0, pady=6)
txt16= tkinter.Text(frame3, height =2, width =4)
txt16.pack(side=RIGHT, anchor=N, expand=0, pady=6)
button2 = tkinter.Label(frame3,text='底标价',font=('楷体',16),bg='#dcdcdc').pack(side=RIGHT, anchor=N, pady=6)


Price = tkinter.Label(top, text='投标价:', font=('楷体',16))
Price.pack(fill=NONE, expand=0, side=TOP, anchor=W, padx=0, pady=0)
frame4 = tkinter.Frame(top,height=20,width=500,relief=RIDGE, bg='#dcdcdc',bd=5,borderwidth=0)
frame4.pack(fill=X,ipady=0,expand=0)
button3 = tkinter.Label(frame4,text='小写',font=('楷体',16),bg='#dcdcdc').pack(side=LEFT, anchor=N, pady=6)
txt17= tkinter.Text(frame4, height =2, width =4)
txt17.pack(side=LEFT, anchor=N, expand=0 ,pady=6)
txt18= tkinter.Text(frame4, height =2, width =4)
txt18.pack(side=LEFT, anchor=N, expand=0,pady=6)
txt19= tkinter.Text(frame4, height =2, width =4)
txt19.pack(side=LEFT, anchor=N, expand=0,  pady=6)
txt20= tkinter.Text(frame4, height =2, width =4)
txt20.pack(side=LEFT, anchor=N, expand=0,  pady=6)
txt21= tkinter.Text(frame4, height =2, width =4)
txt21.pack(side=LEFT, anchor=N, expand=0,  pady=6)
txt22= tkinter.Text(frame4, height =2, width =4)
txt22.pack(side=LEFT, anchor=N, expand=0,  pady=6)
txt23= tkinter.Text(frame4, height =2, width =4)
txt23.pack(side=LEFT, anchor=N, expand=0,  pady=6)
txt24= tkinter.Text(frame4, height =2, width =4)
txt24.pack(side=LEFT, anchor=N, expand=0,  pady=6)

txt25 = tkinter.Text(frame4, height =2, width =4)
txt25.pack(side=RIGHT, anchor=N, expand=0, pady=6)
txt26= tkinter.Text(frame4, height =2, width =4)
txt26.pack(side=RIGHT, anchor=N, expand=0,pady=6)
txt27= tkinter.Text(frame4, height =2, width =4)
txt27.pack(side=RIGHT, anchor=N, expand=0,  pady=6)
txt28= tkinter.Text(frame4, height =2, width =4)
txt28.pack(side=RIGHT, anchor=N, expand=0, pady=6)
txt29= tkinter.Text(frame4, height =2, width =4)
txt29.pack(side=RIGHT, anchor=N, expand=0, pady=6)
txt30= tkinter.Text(frame4, height =2, width =4)
txt30.pack(side=RIGHT, anchor=N, expand=0,  pady=6)
txt31= tkinter.Text(frame4, height =2, width =4)
txt31.pack(side=RIGHT, anchor=N, expand=0,  pady=6)
txt32= tkinter.Text(frame4, height =2, width =4)
txt32.pack(side=RIGHT, anchor=N, expand=0, pady=6)
button4 = tkinter.Label(frame4,text='大写',font=('楷体',16),bg='#dcdcdc').pack(side=RIGHT, anchor=N, pady=6)

Person = tkinter.Label(top, text='投标人:', font=('楷体', 16))
Person.pack(fill=NONE, expand=0, side=TOP, anchor=W, padx=0, pady=6)
frame5 = tkinter.Frame(top,height=20,width=500,relief=RIDGE, bg='#dcdcdc',bd=5,borderwidth=0)
frame5.pack(fill=X,ipady=0,expand=0,pady=0)
button5 = tkinter.Label(frame5,text='会员号码',font=('楷体',16),bg='#dcdcdc').pack(side=LEFT, anchor=N,  pady=2)
txt33 = tkinter.Text(frame5, height =2, width =5)
txt33.pack(side=LEFT, anchor=N, expand=0,pady=2)
txt34 = tkinter.Text(frame5, height =2, width =5)
txt34.pack(side=LEFT, anchor=N, expand=0,pady=2)
txt35 = tkinter.Text(frame5, height =2, width =5)
txt35.pack(side=LEFT, anchor=N, expand=0,pady=2)
txt36 = tkinter.Text(frame5, height =2, width =5)
txt36.pack(side=LEFT, anchor=N, expand=0,pady=2)
txt37 = tkinter.Text(frame5, height =2, width =5)
txt37.pack(side=LEFT, anchor=N, expand=0,pady=2)

txt38 = tkinter.Text(frame5, height =2, width =3)
txt38.pack(side=RIGHT, anchor=N, expand=0, pady=2)
txt39 = tkinter.Text(frame5, height =2, width =3)
txt39.pack(side=RIGHT, anchor=N, expand=0, pady=2)
txt40 = tkinter.Text(frame5, height =2, width =3)
txt40.pack(side=RIGHT, anchor=N, expand=0, pady=2)
txt41 = tkinter.Text(frame5, height =2, width =3)
txt41.pack(side=RIGHT, anchor=N, expand=0, pady=2)
txt42 = tkinter.Text(frame5, height =2, width =3)
txt42.pack(side=RIGHT, anchor=N, expand=0, pady=2)
txt43 = tkinter.Text(frame5, height =2, width =3)
txt43.pack(side=RIGHT, anchor=N, expand=0, pady=2)
txt44 = tkinter.Text(frame5, height =2, width =3)
txt44.pack(side=RIGHT, anchor=N, expand=0, pady=2)
txt45 = tkinter.Text(frame5, height =2, width =3)
txt45.pack(side=RIGHT, anchor=N, expand=0, pady=2)
txt46 = tkinter.Text(frame5, height =2, width =3)
txt46.pack(side=RIGHT, anchor=N, expand=0, pady=2)
txt47 = tkinter.Text(frame5, height =2, width =3)
txt47.pack(side=RIGHT, anchor=N, expand=0, pady=2)
txt48 = tkinter.Text(frame5, height =2, width =3)
txt48.pack(side=RIGHT, anchor=N, expand=0, pady=2)
button6 = tkinter.Label(frame5,text='联系电话',font=('楷体',16),bg='#dcdcdc').pack(side=RIGHT, anchor=N,  pady=2)
frame6 = tkinter.Frame(top,height=20,width=500,relief=RIDGE, bg='#dcdcdc',bd=5,borderwidth=0)
frame6.pack(fill=X,ipady=0,expand=0)
button7 = tkinter.Label(frame6,text='姓名',font=('楷体',16),bg='#dcdcdc').pack(side=LEFT, anchor=N,  pady=6)
txt49 = tkinter.Text(frame6, height =2, width =4)
txt49.pack(side=LEFT, anchor=N, expand=0, pady=6)
txt50 = tkinter.Text(frame6, height =2, width =4)
txt50.pack(side=LEFT, anchor=N, expand=0, pady=6)
txt51 = tkinter.Text(frame6, height =2, width =4)
txt51.pack(side=LEFT, anchor=N, expand=0, pady=6)
txt52 = tkinter.Text(frame6, height =2, width =4)
txt52.pack(side=LEFT, anchor=N, expand=0, pady=6)

txt53 = tkinter.Text(frame6, height =2, width =50)
txt53.pack(side=RIGHT, anchor=N, expand=0, pady=6)
button8 = tkinter.Label(frame6,text='备注',font=('楷体',16),bg='#dcdcdc').pack(side=RIGHT, anchor=N, pady=6)


frame7 = tkinter.Frame(top,height=20,width=500,relief=RIDGE, bg='#dcdcdc',bd=5,borderwidth=0)
frame7.pack(fill=X,ipady=0,expand=0)
button9 = tkinter.Button(frame7,text='修改',font=('楷体',16),bg='#dcdcdc')
button9 .pack(side=RIGHT, anchor=N,padx=12, pady=6)
top.mainloop()
# 设置容器2
#frame2 = tkinter.Frame(top, relief=RIDGE,bg='#3366ff')
#frame2.pack(fill=X, padx=2,pady=10,side=TOP)
# 加一个复选框，一个按键
#chk_text = 'Hex Display'
#int_if_choise = tkinter.IntVar()
#chk1 = tkinter.Checkbutton(frame2,text=chk_text,font=('黑体',12),variable=int_if_choise,onvalue='OK',offvalue='NO')
#chk1.pack(fill=NONE,side=LEFT,padx
