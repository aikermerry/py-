class test():

	def __init__(self):
		self.__num = 5
	def getNum(self):
		return self.__num


	def sets(self,num):
		self.__num =num
	
	nums = property(getNum,sets)

t=test()
t.nums =7
print(t.nums)
