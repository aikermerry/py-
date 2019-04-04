from socket import *
from threading import Thread

#创建套接字

tcpService = socket(AF_INET,SOCK_STREAM)

#BIND LOCAL

Adress = ("",8788)
tcpService.bind(Adress)
tcpService.listen(5)

def lisens(newSocket,clientAdress):
    while True:
        recvData = newSocket.recv(1024)
        if len(recvData)>0:
            
            print("recv:",recvData.decode("utf-8"))

        else:
            print("%s下线了"%clientAdress[0])
            break
        newSocket.send(input("send:").encode("gb2312"))
if __name__ =="__main__":
    while True:
        newSocket,clientAdress = tcpService.accept()
        print("%s已连接"%clientAdress[0])
        th = Thread(target = lisens,args=(newSocket,clientAdress))
        th.start()
    tcpService.close()
    
