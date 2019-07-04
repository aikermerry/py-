from threading import Thread
import time
num = 1
def test():
    global num
    num +=1
    time.sleep(2)
    print("执行一个程序")
    
    

for i in range(5):
    t = Thread(target=test)
    t.start()

print(num)
