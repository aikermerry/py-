
from threading import Thread
from socket import *
#第一步发消息
def sendMwssage():
    while 1:
        message = input(">> ")
        udpSocket.sendto(message.encode("utf-8"),("192.168.1.104",8080))
#接收消息
def recvMessage():
    udpSocket.bind(("",6789))
    while 1:
        recv = udpSocket.recvfrom(1024)
        print("\r%s"%"<< "+recv[0].decode("utf-8"),end="\n>> ")

def main():
    global ip,port,udpSocket
    udpSocket = socket(AF_INET,SOCK_DGRAM)
    tx = Thread(target=sendMwssage)
    rx = Thread(target=recvMessage)
    ip = input("输入对方ip:")
    port = int(input("输入对方port:"))
    
    tx.start()
    rx.start()

    tx.join()
    rx.join()

if __name__=="__main__":
    main()
