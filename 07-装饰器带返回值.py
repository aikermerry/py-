def loc(fuc):
    def zhuangshiqi(*args,**kwargs):
        print("执行装饰器1")
        recall = fuc()
        return recall
    return zhuangshiqi
@loc
def test():
    print("装饰器共同工作")

def test2():
    print("我有返回值")
    return "返回值"

def test3(a):
    print("我带参数传入")
    print(a)

print('还没调用')
x = test()

print(x)

