# coding:utf-8

class Test(object):
    def __init__(self):
        pass
    def __getattr__(self, item):
        print(item)
        return self


print(Test().a.s)