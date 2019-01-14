class test():

	def __init__(self):
		self.__num = 5
	
	def sets(self,num):
		self.__num =num
	
	def getNum(self):
		return self.__num

	nums = property(getNum,sets)

t=test()
t.nums =7
print(t.nums)
