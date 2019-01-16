
#齐波拉契数列
def test(num):
    print("_______start_______")
    a,b =0,1
    for i in range (num):
        yield b 
        a,b =b,a+b
    print("_________end_____")


a= test(5)

print(next(a))

print(next(a))
print(next(a))
print(next(a))
print("下面用的方法是__next__")
print(a.__next__())

b= test(5)

print("下面用的是循环的方式来取生成器生成的值")

for i in b:
    print(i)




