import os
from multiprocessing import Pool
import time

def test(num):
    print("我是创建的进程%d"%num)
    time.sleep(1)
    print("这个进程的id 是%d"%os.getpid())

pool1 = Pool(3)


for i in range(1,10):
    pool1.apply_async(test,(i,))
    print("我添加了进程%d"%i)

pool1.close()
pool1.join()
print("结束进程")
