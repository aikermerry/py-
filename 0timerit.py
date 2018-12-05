import timeit

def test1():
    li = []
    for i in range(10000):
        li.append(i)
tl = timeit.Timer("test1","from __main__ import test1")
print(tl.timeit(number = 1000))
