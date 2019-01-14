
def unlock(fuc):
    def zhuangshiqi():
        print("执行装饰器")
        return fuc()
    return zhuangshiqi


@unlock
def test():
    print("装饰器共同工作")

#调用
print('还没调用')
test()
