def loc(fuc):
    def zhuangshiqi():
        print("执行装饰器1")
        return fuc()
    return zhuangshiqi

def unlock(fuc):
    def zhuangshiqi():
        print("执行装饰器")
        return fuc()
    return zhuangshiqi

@loc
@unlock
def test():
    print("装饰器共同工作")

#调用
print('还没调用')
test()
