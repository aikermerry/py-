import socket
import struct
def main():
#UDP传输每次都要将IP和端口加上
    socket1 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    while 1:
        data = input("输入数据")

        #socket1.sendto(struct.pack("!HH",data.encode("utf-8")),("192.168.1.104",5678))
        socket1.sendto(struct.pack("!HH",4,1),("192.168.1.104",5678))
if __name__ == "__main__":
    main()
