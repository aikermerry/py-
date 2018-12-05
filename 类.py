class SweetPotato:
	"""docstring for SweetPotato"""
	def __init__(self):
		self.cookedLevel = 0
		self.cookedString = "新鲜的"
		self.addCooking = []	
	def  __str__(self):
		msg = "生熟程度："+self.cookedString
		msg += " 烧烤级别："+str(self.cookedLevel)
		if len(self.addCooking)>0:
			msg += " 添加的调料："
			for arg in self.addCooking:
				msg += arg 
				msg += ","
			msg = msg[:-1]
		else:
			msg += " 未添加调料"
		return msg
	def addCondiment(self,arg):
		self.addCooking.append(arg)
	def classCooking(self,num):
		self.cookedLevel +=num
		if self.cookedLevel>10:
			self.cookedString = "材料损坏"
		elif self.cookedLevel>7:
			self.cookedString = "食物熟了"
		elif self.cookedLevel>4:
			self.cookedString = "食物半生不熟"
		else:
			self.cookedString = "食物还是生的"
diGua = SweetPotato()
while 1:
	level = int(input("火候："))
	cookings = input("调料：")
	
	diGua.addCondiment(cookings)

	diGua.classCooking(level)

	print(diGua)
