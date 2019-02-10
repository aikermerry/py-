import os
from multiprocessing import Process,Queue
import time

def getMsg(msg):
    while 1:
         time.sleep(1)
        # msg.put("shenmn")

def pushMsg(msg):
    while 1:
         print("\n"+msg.get()+"!")
         time.sleep(1)
def main():
    q = Queue()
    p = Process(target=getMsg,args=(q,))
    p1 = Process(target=pushMsg,args=(q,))
    p.start()
    p1.start()
    while 1:
        q.put(input("亲输入:"))
if __name__ == "__main__":
    main()
