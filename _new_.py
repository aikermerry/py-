class A(object):
    def __init__(self):
        print("这是init方法")
#    def __new__(cls):#new方法至少必须有一个cls
#
 #       print("这是new方法")
  #      return object.__new__(cls)#必须有返回

class Singleton:
    __instance = None
    __fist_init = False
    def __new__ (cls,age,name):#保持地址不变实例化是调用的都是同一个地址内的内容:
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance
    def __init__(self,age,name):
        if not self.__fist_init:
            self.age = age
            self.name = name
            Singleton.__fist_init = True

a = Singleton(18,"f")
b = Singleton(8,"g")
print(id(a))
print(id(b))
print(a.age)
print(b.age)
a.age = 19
print(b.age)
