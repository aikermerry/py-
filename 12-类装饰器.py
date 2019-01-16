class Test():
    def __init__(self,func):
        print("-----test---%s"%func)
        self.__func = func
        
    def __call__(self):
        print("我在测试" )
        self.__func()

@Test
def test():
    print("-----test--")


test()
