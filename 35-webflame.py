import time

from mywebflam import *


class Application(object):
    """用户通用框架不做任何修改"""
    def __init__(self,url):
        self.url = url

    def __call__(self, env, start_response):
        path = env.get("PATH_INFO","/")
        for url,app in self.url:
            if url == path:
                return app(env, start_response)

        status = "404 load failed"
        headers = {
            ("Content-Type", "text/plain;charset=utf-8"),
            ("Service", "My server")
        }
        start_response(status, headers)
        return "open filed"


def index(env, start_response):
    status = "200 OK"
    headers = {
        ("Content-Type", "text/plain;charset=utf-8"),
        ("Service","My server")
    }
    start_response(status, headers)
    return "你好"

def ctime(env, start_response):
    status = "200 OK"
    headers = {
        ("Content-Type", "text/plain;charset=utf-8"),
        ("Service","My server")
    }
    start_response(status, headers)
    return time.ctime() + "你好"


#路由：可以提供用户自己定义接口操作
url= {
    ("/",index),
    ("/ctime",ctime)
}


app = Application(url)
http_service = HttpServices(app)
http_service.set_port(8087)
http_service.start()





