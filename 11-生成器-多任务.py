import time
def test1():
    num = 0
    while True:
        print(num)
        yield num 
        num+=1
def test2():
    num1 = 50
    while True:
        print(num1)
        yield num1
        num1-=1
a= test1()
b=test2()
while True:
    b.__next__()
    a.__next__()
    time.sleep(1)
