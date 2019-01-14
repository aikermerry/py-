from collections import Iterable

print(isinstance([],Iterable))

print(isinstance({},Iterable))

from collections import Iterator

print(isinstance((x for x in range(10)),Iterator))

print("iter()函数的使用，现在使用生成器")
print("列表")
print(iter([]),Iterator)

print('“字符串”')

print(iter("abc"),Iterator)


