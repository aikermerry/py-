# coding:utf-8
import time


def application(env, start_response):
    status = "200 OK"
    headers = {
        ("Content-Type", "text/plain;charset=utf-8"),
        ("Service","My server")

    }
    start_response(status, headers)
    return time.ctime() + "你好"
