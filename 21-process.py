import os
import time
from multiprocessing import Process

class test(Process):
        
    def run():
        while 1:
            print("我是子程序")
p = test()

p.start()
while 1:
    print("我是父程序")
