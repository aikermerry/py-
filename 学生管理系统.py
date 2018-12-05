# 管理系统
data = []


# 添加名片
def addData():
	name = input("请输入姓名：")
	age = input("请输入年龄：")
	sex = input("请输入性别：")
	phone = input("请输入电话号码：")
	idcard = input("请输入身份验证 ID：")
	message = {
	"name" : name,
	"age"  : age,
	"phone": phone,
	"sex"  : sex,
	"ID"   : idcard, 
	}
	data.append(message)
# 删除数据
def delData():
	name = input("请输入需要删除人的姓名：")
	num = 0
	while len(data):
		for i in data:
			if i["name"] == name:
				break
			num += 1
		if num < len(data):
			break	
		if num >= len(data):
			name = input("输入有误，请重新输入或输入exit退出操作：")
			num = 0
			if name == "exit":
				return 0	

	if num != len(data) and len(data):
		Id = input("请输入个人ID以执行操作：")
		while True:
			if data[num]["ID"] == Id:
				print("删除 %s的信息成功"%data[num]["name"])
				del data[num]
				break
			else:
				Id = input("ID错误，请重新输入或输入exit退出操作：")
				if Id == "exit":
					return 0
	if len(data) == 0:
		print("数据为空") 


# 查询
def findDate():
	name = input("请输入需要查询的姓名：")
	num = 0
	for i in data:
		if i["name"] == name:
			break
		num += 1
	if num == len(data):
		if len(data) == 0:
			print("数据为空")
		else:
			print("无此人信息")
	else:
		print("------------------------")
		for m, n in data[num].items():
			print(m+":"+n)
		print("------------------------")


# 修改数据
def fixData():
	name = input("请输入需要修改的姓名：")
	num = 0
	while len(data):
		for i in data:
			if i["name"] == name:
				break
			num += 1
		if num < len(data):
			break
		if num >= len(data):
			name = input("输入错误，请重新输入或输入exit退出操作：")
			num = 0
			if name == "exit":
				return 0
	
	if num < len(data):
		while True:
			fixedMessage = input("请输入需要修改的内容name:姓名，age:年龄，phone:电话，sex：性别：")
			try:
				if fixedMessage == "ID":
					print("不可修改")
				else:	
					print("当前为:"+data[num][fixedMessage])
					data[num][fixedMessage]=input("%s修改为："%fixedMessage)
					print("修改成功")
			except:
				print("输入错误请重新输入")
			
			justge = input("输入任意继续或者输入exit退出:")
			if justge == "exit":
					return 0
	
	if len(data) == 0:
		print("数据为空")


def main():
	while True:		
		try:
			slects = eval(input("1：添加，2：查询，3：删除，4：修改,5：退出。请输入操作编号："))
			if slects <= 5:
				break
			else:
				print("无此选项")
		except:
			print("你输入有误请重新输入")
	
	if slects == 1:
		addData()
	if slects == 2:
		findDate()
	if slects == 3:
		delData()
	if slects == 4:
		fixData()
	if slects == 5:
		exit()


while True:
	main()
