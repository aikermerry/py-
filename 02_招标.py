# 这是用来获取学校告示，为了得到最新的招标信息
import urllib.request
from urllib import  request
from bs4 import BeautifulSoup
import re
import time
import itchat
import os
from tkinter import *  


class MyGlobal:
    def __init__(self):
        self.xiHuaUrl = "http://www.xhu.edu.cn/18/list1.htm"
        self.commentSignl = 0
        self.scanNnmber = 1
        self.soupArticle = ""

class Gui_set:
    def __init__(self):
        self.init_window_name=Tk() 
       
    def windowSet(self):
        self.init_window_name.title("西华大学爬虫")      #窗口名
        self.init_window_name.geometry('320x128+10+10')                 #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name["bg"] = "pink"                            #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        self.init_window_name.attributes("-alpha",0.9) 
        self.label = Label(self.init_window_name, text='Hello',font='Helvetica -12 bold') #创建标签
               #虚化，值越小虚化程度越高
        self.tst = Text( self.init_window_name,width =50)
        self.tst.place(x=90,y=45,width = 150,height= 25)
        self.tst.insert("0.0","Welcom !!!! ")
       

    def buttonSet(self):
        self.buttonSets0= Button(self.init_window_name, text="开始", bg="lightblue", width=5,height=1,command=self.mian)# 调用内部方法  加()为直接调用
        self.buttonSets0.grid(row=0, column=0, padx=5, pady=5)
        self.buttonSets1= Button(self.init_window_name, text="结束", bg="lightblue", width=5,height=1,command=self.init_window_name.destroy)  # 调用内部方法  加()为直接调用
        self.buttonSets1.grid(row=0, column=2,padx=175,pady=5)
        Label(self.init_window_name,text="程序运行中：").grid(row=3,sticky=W)

    
    def mian(self):
        print("start........")

        wechat = ItChat("刘")
        get_msg =GetMesg()
        globa = MyGlobal()
        while True:
            get_msg.getTime(globa)
            get_msg.getAdvertisement(wechat, globa)
            time.sleep(1)

# 调用itchat登录，使用hotReload=True来讲登录信息加入到缓存区，避免短时间段开连接再次扫码登录
class ItChat:
    def __init__(self,Name):  
        itchat.auto_login(hotReload=True)
     # 查找特定的人获取其ID,现在的版本的ID不是固定的，不断的在更新
        self.user = itchat.search_friends(Name)[0]['UserName']
    def seedMsg(self):
        itchat.send_file("zb.txt", toUserName=self.user)


class DataGet(object):
    """docstring for DataGet"""
    def recoverData(self):
        with open("zb.txt","r") as f:
            self.text = f.readline()

        
class GetMesg():
    getlLine = DataGet()   
    def getContentOrComment(self, globa): # 模拟浏览器解析网址
        headers = {'User-Agent':  'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) Ap'
                                  'pleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        req=request.Request(url=globa.xiHuaUrl, headers=headers)
        self.response = urllib.request.urlopen(req).read()
        globa.soupArticle = BeautifulSoup(self.response, 'hml.parser')
    
    def getTime(self, globa):
        #self.commentTime = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        self.commentDayTime = time.strftime('%H-%M-%S', time.localtime(time.time()))
        if self.commentDayTime == '12-00-00' or self.commentDayTime == '19-01-00':  # 判断是非在这个特定的时间，是这个时间，程序产生效果 
            globa.commentSignl = 1
    
    def writData(self):
        self.num =0
        with open(r"zb.txt", "w+") as document:
                for commentNewTitle in globa.soupArticle.find_all(attrs='column-news-item'):
                    commentTitle = commentNewTitle.get_text()
                    if re.search(r'招标', commentTitle, re.M | re.I):
                        document.write('%d. %s' % (self.num, commentTitle)+'\n')
                        self.num += 1    

    def getAdvertisement(self,chat, globa):
        if not os.path.exists("zb.txt"):
            self.getContentOrComment(globa)
            self.writData()
            chat.seedMsg()   
        else:
            if globa.commentSignl == 1:
                self.getlLine.recoverData()
                self.getContentOrComment(globa) 
                print('采集次数:', globa.scanNnmber)
                globa.scanNnmber += 1
                globa.commentSignl = 0
                if self.getlLine.text[3:-1] != globa.soupArticle.find_all(attrs='column-news-item')[0].get_text():
                    self.writData()
                    chat.seedMsg() 
                else:
                    print("数据未更新")

               


l=Gui_set()
l.windowSet()
l.buttonSet()
l.init_window_name.mainloop()  

