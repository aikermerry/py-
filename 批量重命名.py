print("文件批量重命名")

import os
showList = os.listdir()
flimType = input("请输入文件类型（txt/doc/exe....）：")
newName = input("新文件名：")
typeName = input("输入需要更改的文件类型，不更改则跳过：")
num = 0
if len(typeName)>0:
	flimTypes = typeName
else:
	flimTypes =flimType 
	
newNames =""
for i in showList:
	dr = i.rfind(".")
	if dr >=0:
		if flimType == i[dr+1:]:

			newNames = newName+"%d"%num+"."+flimTypes
			print(i+"--->"+newNames)
			os.rename(i[0:],newNames)
			num +=1
			