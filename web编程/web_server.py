#做一个静态的WEB服务器
#tcp socket 服务器
from socket import *
from multiprocessing import Pool
import time 
#建立tcp链接端
socket = socket()

#绑定ip

socket.bind(("",8086))
#模仿网页获取数据的功能
socket.listen(5)

def DealMesg(newSocket):
    ##收到消息
    print("处理获取到的消息（获取报文头）")
    message = newSocket.recv(1024)

    print(message)
    ##处理获取到的消息（获取报文头）


    ##得到报文头（去本地查找HTTP请求的文件）

    #将获取到的文件内容读取出来并发送回去
def main():
    #建立进程池如果检测到有请求就将任务丢进进程内执行
    pool = Pool()
    while True:
        print("等待链接...")
        newSocket,clientAdress=socket.accept()
        pool.apply_async(DealMesg,args=(newSocket,))
        time.sleep(1)



    pool.close()
    socket.close()





if __name__ == '__main__':
    main()


