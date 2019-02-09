import os 
import time

ret = os.fork()

print(ret)

if ret :
    while True:
        print("我")
        time.sleep(1)
        print(os.getpid())

else :
    while True:
        print("你")
        print(os.getpid(),os.getppid())
        time.sleep(1)
