# coding:utf-8
import re
from socket import *
from threading import *
import sys
import netifaces as ni


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
        """实现字符串的拼接"""
        self.response_header = "HTTP/1.1 " + status + "\r\n"
        for i in headers:
            self.response_header += "%s:%s\r\n" % i

    def remote_recv(self, newSocket):
        "接收数据"
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

        newSocket.send(bytes(response, "utf-8"))
        newSocket.close()

    def set_port(self, port):
        self.tcpService.bind(("", port))


def get_Net_Local_Ip():
    try:
        ni.ifaddresses('enp2s0')
        netIp = ni.ifaddresses('enp2s0')[2][0]['addr']
        return netIp
    except:
        my_ip_name = getfqdn(gethostname())
        # 获取本机ip
        myaddr = gethostbyname(my_ip_name)
        return myaddr


def main(port):
    #动态加载框架
    #python HttpService.py webFramwork app
    try:
        _,modename,classmethod =sys.argv
    except:
        sys.exit("python HttpService.py webFramwork app")
    mode_names = __import__(modename)
    app = getattr(mode_names,classmethod)
    http_service = HttpServices(app)
    http_service.set_port(port)
    http_service.start()

if "__main__" == __name__:
    print("服务器启动。。。。。")
    port = 8087
    localIp = get_Net_Local_Ip()
    print(localIp+":%d"%port)

    main(port)
