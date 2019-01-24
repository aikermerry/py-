import functools

def showarg(*arg,**kwarg):
    print(arg)
    print(kwarg)


p1 = functools.partial(showarg,1,2,3)

()

p1(4,5,6)


p1(a=4,b=6)


