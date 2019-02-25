from threading import Thread
import time
import threading
num = 1
def test():
    global num
    mutex.acquire()
    for i in range(1000000):
        num +=1
    mutex.release()
    print("执行第一个程序:%d"%num)
def test2():
    global num
    mutex.acquire()
    for i in range(1000000):
        num +=1
    mutex.release()
    print("执行第二个程序:%d"%num)
#创建锁
mutex = threading.Lock()

t = Thread(target=test)
t2 = Thread(target=test2)
t2.start()
t.start()

print(num)
