import socket
import time
socket1 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#socket1.sendto(b"dsk",("192.168.1.102",8080))
port = ("",2555)

socket1.bind(port)
while 1:
    recvData = socket1.recvfrom(1024)
    contment,address =recvData
    date = time.asctime()+":"
    
    print(date,contment.decode("utf-8"))
