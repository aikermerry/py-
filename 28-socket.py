import socket
def main():
#UDP传输每次都要将IP和端口加上
    socket1 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    while 1:
        data = input("输入数据")
        socket1.sendto(data.encode("utf-8"),("192.168.1.101",2555))
if __name__ == "__main__":
    main()
