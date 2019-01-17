Test = type ("test2",(),{})
#这样就创建了一个类,
#第一个参数是类的名字
#第二个是类继承的类名字没有就为空元组
#第三个是参数,没有就为空字典
print(type(Test))

##ex:
Test2 = type("Test2",(),{"num":2})
print(Test2.num)


def printNum():
    print("num")

test = type("Test3",(),{"printNum":printNum})

test.printNum()

