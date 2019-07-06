# coding:utf-8
import re
from socket import *
from threading import *


# 建立tcp通信


class HttpServices(object):
    def __init__(self,app):
        """app 就是web框架"""
        self.tcpService = socket(AF_INET, SOCK_STREAM)
        self.response_header = ""
        self.response_start = ""
        self.app = app

    def start(self):
        self.tcpService.listen(50)
        while True:
            newSocket, newAddress = self.tcpService.accept()
            web_thread = Thread(target=self.remote_recv, args=(newSocket,))
            web_thread.start()

    def start_respond(self, status, headers):
        self.response_header = "HTTP/1.1 " + status + "\r\n"
        for i in headers:
            self.response_header += "%s:%s\r\n" % i

    def remote_recv(self, newSocket):

        recvData = newSocket.recv(1024)
        recvData = recvData.decode("utf-8")
        print(recvData)
        if len(recvData) == 0:
            newSocket.close()
            return 0
        path = re.findall(".*GET(.*)HTTP.*", recvData)
        print(path[0].split()[0])
        path = path[0].split()[0]

        #请求体
        env = {
            "PATH_INFO": path,
        }
        response_body = self.app(env, self.start_respond)

        response = self.response_header + "\r\n" \
                   + response_body
        print(response)
        newSocket.send(bytes(response, "utf-8"))
        newSocket.close()

    def set_port(self, port):
        self.tcpService.bind(("", port))


def main():
    http_service = HttpServices()
    http_service.set_port(8086)
    http_service.start()


if "__main__" == __name__:
    print("服务器启动。。。。。")
    main()
