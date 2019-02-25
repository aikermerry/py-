# 这是用来获取学校告示，为了得到最新的招标信息
import urllib.request
from urllib import request
from bs4 import BeautifulSoup
import re
import time
import itchat
import os
              
class MyGlobal:
    def __init__(self):
        self.xiHuaUrl = "http://www.xhu.edu.cn/18/list1.htm"
        self.commentSignl = 0
        self.scanNnmber = 1
        self.soupArticle = ""
     
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
        with open("zb.txt", "r") as f:
            self.text = f.readline()

        
class GetMesg():
    getlLine = DataGet()   
    def getContentOrComment(self, globa): # 模拟浏览器解析网址
        headers = {'User-Agent':  'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) Ap'
                                  'pleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        req=request.Request(url=globa.xiHuaUrl, headers=headers)
        self.response = urllib.request.urlopen(req).read()
        globa.soupArticle = BeautifulSoup(self.response, 'html.parser')
    
    def getTime(self, globa):
        #self.commentTime = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        self.commentDayTime = time.strftime('%H-%M-%S', time.localtime(time.time()))
        if self.commentDayTime == '12-00-00' or self.commentDayTime == '18-31-00':  # 判断是非在这个特定的时间，是这个时间，程序产生效果
            globa.commentSignl = 1
    
    def writData(self):
        self.num = 0
        with open(r"zb.txt", "w") as document:
                for commentNewTitle in globa.soupArticle.find_all(attrs='column-news-item'):
                    commentTitle = commentNewTitle.get_text()
                    if re.search(r'招标', commentTitle, re.M | re.I):
                        document.write('%d. %s' % (self.num, commentTitle)+'\n')
                        self.num += 1    

    def getAdvertisement(self, chat, globa):
        if not os.path.exists("zb.txt"):
            self.getContentOrComment(globa)
            self.writData()
            chat.seedMsg()   
        else:
            if globa.commentSignl == 1:
                globa.commentSignl = 0
                self.getlLine.recoverData()
                self.getContentOrComment(globa) 
                print('采集次数:', globa.scanNnmber)
                globa.scanNnmber += 1
                tmp_txt = globa.soupArticle.find_all(attrs='column-news-item')[0].get_text()
                if self.getlLine.text[3:-1] != tmp_txt and re.search(r'招标', tmp_txt, re.M | re.I):
                    self.writData()
                    chat.seedMsg() 
                else:
                    print("数据未更新")

               
if __name__ == "__main__":
    wechat = ItChat("张老师")
    print("start........")
    get_msg =GetMesg()
    globa = MyGlobal()
    uuid = itchat.get_QRuuid()
    while True:
        try:
            get_msg.getTime(globa)
            get_msg.getAdvertisement(wechat, globa)
            time.sleep(1)
        except:
            print("liu")
            pass











