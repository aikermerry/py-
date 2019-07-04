import os
from multiprocessing import Process
import time 

def test():
    while 1:
        
        print("我是子程序")
p = Process(target=test)

p.start()

print("我是父程序")


