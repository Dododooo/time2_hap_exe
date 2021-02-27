
import datetime
from tkinter import *
import sys
import os
#字符串化当前时间
time_now=str(datetime.datetime.now())
#设定hap时间与当前时间格式化
time_happy='2021-02-23 17:30:00'
time_now=time_now[0:19]
month='{:02d}'.format(datetime.datetime.now().month)
month_1=month[0]
month_2=month[1]
day='{:02d}'.format(datetime.datetime.now().day)
day_1=day[0]
day_2=day[1]
time_happy = time_happy[:5] + month_1+ month_2 + time_happy[7:8]+day_1+ day_2 +time_happy[10:]
d1 = datetime.datetime.strptime(time_now, '%Y-%m-%d %H:%M:%S')
d2 = datetime.datetime.strptime(time_happy, '%Y-%m-%d %H:%M:%S')
time_count=d2-d1


seconds=int(time_count.seconds)
m, s = divmod(seconds, 60)
h, m = divmod(m, 60)
combine_time=int(str(datetime.datetime.now().hour).zfill(2)+str(datetime.datetime.now().minute).zfill(2))


tk_bg = Tk()
tk_bg.title("还有多久下班")
if combine_time > 1730:
    lb1 = Label()
    # 创建一个输出框控件
    w = PhotoImage(file="res\\background.gif")
    # 创建一个图片对象，图片只能是gif
    lb1["image"] = w
    # 关联图片到控件
    lb1.pack()
    lb = Label()
    # 创建一个输出框控件
    lb["text"] = "已经下班啦，当前时间是:" , time_now
    lb["width"] = 40
    # 设置该控件左右宽度
    lb["height"] = 1
    # 设置该控件上下高度
    lb.pack()
    # 显示控件
    # 显示控件
    lb = Label()
    lb["text"] = "by Hysterical-byte-f**k BYD"

    # 写入文本
    lb["width"] = 50
    # 设置该控件左右宽度
    lb["height"] = 1
    # 设置该控件上下高度
    lb.pack()

    # 显示窗口
    def close_window():
        tk_bg.destroy()
    bm=Button(text = "yeeeeaah",command = close_window)

    #写入文本
    bm.pack()
    #显示控件
    tk_bg.mainloop()
    #显示窗口
else:
#窗口名称
    lb1 = Label()
    # 创建一个输出框控件
    w = PhotoImage(file="res\\pic.gif")

    lb1["image"] = w
    # 关联图片到控件
    lb1.pack()
    lb=Label()
    #创建一个输出框控件
    lb["text"]= "还有%d:%02d:%02d下班" % (h, m, s)
    lb["width"]=50
    #设置该控件左右宽度
    lb["height"]=1
    #设置该控件上下高度
    lb.pack()
    #显示控件
    lb=Label()
    lb["text"]='还有{}秒'.format(time_count.seconds)
    lb["width"]=50
    #设置该控件左右宽度
    lb["height"]=1
    #设置该控件上下高度
    lb.pack()
    #显示控件
    lb=Label()
    lb["text"]="当前时间：",time_now


    #写入文本
    lb["width"]=50
    #设置该控件左右宽度
    lb["height"]=1
    #设置该控件上下高度
    lb.pack()
    lb=Label()
    lb["text"]="by Hysterical-byte-f**k BYD"



    #写入文本
    lb["width"]=50
    #设置该控件左右宽度
    lb["height"]=1
    #设置该控件上下高度
    lb.pack()
    #显示控件


    def close_window():
        tk_bg.destroy()
    bm=Button(text = "好的吧",command = close_window)

    #写入文本
    bm.pack()
    #显示控件
    tk_bg.mainloop()
    #显示窗口



def resource_path(relative_path):
    if getattr(sys, 'frozen', False): #是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
filename = resource_path(os.path.join("res","background.gif"))
filename_2= resource_path(os.path.join("res","pic.gif"))
input('press any button to quit')