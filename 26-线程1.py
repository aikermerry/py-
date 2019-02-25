from threading import Thread
import time
num = 1
def test():
    global num
    num +=1
    print("执行一个程序")
    time.sleep(1)
    

for i in range(5):
    t = Thread(target=test)
    t.start()

print(num)
