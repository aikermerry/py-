
def loc_arg(strs="kong"):
    def loc(fuc):
        def zhuangshiqi(*args,**kwargs):
            print("执行装饰器1",strs)
            recall = fuc()
            return recall
        return zhuangshiqi
    return loc
@loc_arg(" 带有参数的装饰器 ")
def test():
    print('还没调用')
x = test()

print(x)

