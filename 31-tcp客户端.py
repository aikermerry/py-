from socket import *

clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect(("192.168.31.250",8080))

#发送消息
clientSocket.send("wosi开始 liuliwn ".encode("gb2312"))
recvData = clientSocket.recv(1024)

print(recvData.decode("utf-8"))

clientSocket.close()
