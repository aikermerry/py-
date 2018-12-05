class Person(object):
	"""docstring for Person"""
#私有属性为在变量前面加上 __ 两个下划线。只能内部访问，在外部不可访问域修改
	def __init__(self, arg,age):
	
		self.arg = arg
		self.age = age
	def  sh(self):
		self.age = 2

		pass


class Person2(Person):
	
	
	def setAeg(self):
		self.age1 = 10
		
	
Persons = Person(1,5)

print(Persons.age)
Persons.sh()
print(Persons.age)