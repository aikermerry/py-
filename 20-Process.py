import os
from multiprocessing import Process


def test():
    while 1:
        print("我是子程序")
p = Process(target=test)

p.start()
while 1:
    print("我是父程序")
