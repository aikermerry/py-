# coding:utf-8


from MysqlHelper import *

params = ["fedddr","2"]
sql = "UPDATE xiaoliu SET name=%s WHERE id<%s"

mysql_helper = MysqlHelper(host="localhost",user="root",passwd="123456",port=3306,db='python')

# mysqls.cud(sql,params)
# sql = "select *from xiaoliu;"
# params=[]
# print(mysqls.find_get(sql,params))
mysql_helper.cud("update xiaoliu set age=3;")

mysql_helper.find_get("select *from xiaoliu;")
mysql_helper.show_result()