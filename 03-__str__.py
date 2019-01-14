class Test():
	def test(self):
		print("你好我在测试")
	def __str__(self):
		return "你好我是__str__"

#实例化类

test1 = Test()

print(test1)
test1.test()
