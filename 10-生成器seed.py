def test():
    print("start")
    i = 0
    while i<5:
        temp = yield i
        i+=1
a = test()
a.__next__()

a.send("s")
