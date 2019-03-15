from socket import *
import struct
from threading import Thread
#模拟tftp 下载
#发送一个下载请求
#1.收到服务器返回收到
#2.服务器判断是否存在数据，存在返回数据。不存在返回一个错误
#3.接收数据，如果数据包大于512个字节，就分数据包发送。
#4.建立多线程

def sendCmd():
    files ="test.jpg"
    files = files.encode("utf-8")
    fileName = struct.pack("!H8sb5sb",1,files,0,"octet".encode("utf-8"),0)
    udpSocket.sendto(fileName,(connect_Ip,connect_Port))
    print("发送下载指令") 
   
   
def recvBack():  
    data = udpSocket.recvfrom(1024)
    print(data)
    if struct.unpack("!HH",data)[0] ==4:
       recvedFile = open("test.jpg","wb")
       num1 = 1
       while True:
            data  = udpSocket.recvfrom(1024)
            cmData =struct.unpack("!HH", data[:4])
            num1 = cmData[1]
            if cmData[0]==3:
                recvedFile.write(data[4:])
                ack = struct.pack("!HH",4,num1)
                udpSocket.sendto(ack,(connect_Ip,connect_Port))
            elif  len(data)<516:break
            elif cmData[0]!=3:print("出错了。下载失败");break
       recvedFile.close()
       print("下载完毕")
    print("结束。。。。。")


def mian():
    global connect_Ip,connect_Port,local_Port,udpSocket
    local_Port = int(input("设置本地端口号xxxx:"))
    connect_Ip = input("输入连接的地址x.x.x.x:")
    connect_Port =int( input("输入端口xxxx："))
    tx = Thread(target=sendCmd)
    rx = Thread(target=recvBack)
    udpSocket = socket(AF_INET,SOCK_DGRAM)
    udpSocket.bind(("",local_Port))

    rx.start()
    tx.start()


if __name__=="__main__":
    mian()
