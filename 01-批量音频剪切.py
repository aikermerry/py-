from pydub import AudioSegment
import os
from mutagen.mp3 import MP3
'''
****** 设置一下是否启动剪切文件数量限制 ******

set_on= True 启动
set_on = False 关闭
set_num 为设置的限制数量

****************************************
'''
set_num = 5
set_on=False
#设置剪切时间
jianqielen = 3
#不填默认获取当前路径下的文件,否者获取特定路径下的文件
showList = os.listdir()
nums =0
print("*************开始剪切*******************\n")
for name in showList:
   try:
      print("**"*20+"\n")
      print("正在剪切:"+name+"\n")
      file_name = (name)
      sound = AudioSegment.from_mp3(file_name)
      audio = MP3(file_name)
      audio_time=(int)(audio.info.length)#计算MP3文件长度以秒为单位
      #计算有多少个剪切长度
      N=audio_time//jianqielen
      minutes = 0
      for i in range(0,N):
         start  = i*jianqielen
         end  = min(start+jianqielen,audio_time)

         if start>=60:
            start = start-60
         if end>=60:
            end = end-60
            minutes +=1

         #00:00,23:59
         start_time="%d:%d"%(minutes,start)
         stop_time="%d:%d"%(minutes,end)
         save_name=name[0:-4]+"%d.mp3" %i
         start_time = (int(start_time.split(':')[0])*60+int(start_time.split(':')[1]))*1000
         stop_time = (int(stop_time.split(':')[0])*60+int(stop_time.split(':')[1]))*1000
         word = sound[start_time:stop_time]
         word.export(save_name, format="mp3")
   except :
      print("有不是mp3格式的文档哟,文件是"+name)
   nums+=1
   if set_on:
      if nums ==set_num :
         break


print("*************结束剪切*******************\n")



            
              
