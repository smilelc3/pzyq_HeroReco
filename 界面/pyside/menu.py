import tkinter

root = tkinter.Tk()
menubar = tkinter.Menu(root)
filemenu = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label='文件', menu=filemenu)
filemenu.add_command(label='新建')
filemenu.add_command(label='打开')
filemenu.add_command(label='保存')
#filemenu.add_separator() 分割线

helpmenu = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label='配置', menu=helpmenu)
helpmenu.add_command(label='图片参数')
helpmenu.add_command(label='扫描仪参数')

testmenu = tkinter.Menu(menubar,tearoff=0)
menubar.add_cascade(label='开始扫描',menu=testmenu)
testmenu.add_command(label='开始扫描')

root.config(menu=menubar)
root.geometry('200x400')
root.mainloop()
