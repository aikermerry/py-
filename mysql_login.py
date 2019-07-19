# coding:utf-8

import hashlib

from MysqlHelper import *


class CheckLogin():

    def __init__(self):
        self.mysql_helper = MysqlHelper(host="localhost", user="root", passwd="123456", port=3306, db='python')

    def get_message(self):
        self.username = input("用户名：")
        self.password = input("密码：")

        hash_password = hashlib.sha1()
        hash_password.update(self.password.encode("utf-8"))
        self.hash_password = hash_password.hexdigest()
    def judge_user(self):
        sql = "select passwd from user_passwd where username=%s"
        params = [self.username]
        self.result = self.mysql_helper.find_get(sql, params)

    def login(self):

        self.get_message()
        #user_passwd
        self.judge_user()
        if self.result ==():
            print("\n用户不存在，请注册")
            register = input("是否注册[Y/N]:")
            if register.lower() == "y":
                self.register()
            else:
                print("成功退出")
        else:
            if self.result[0][0]==self.hash_password:
                print("\n*******登录成功********")
            else:
                print("\n密码错误")
    def register(self):
        self.get_message()
        self.judge_user()
        if self.result == ():
            sql = "insert into user_passwd values(0,%s,%s);"
            params = [self.username,self.hash_password]
            self.mysql_helper.cud(sql,params)
        else:
            print("用户已存在，请登录")
            login = input("是否登录[Y/N]:")
            if login.lower() == "y":
                self.login()
            else:
                print("成功退出")
if __name__ == '__main__':
    check_login = CheckLogin()
    print("V1.1 login system\n")
    judge = input("请选择登录还是注册：[1/2]:")
    if judge == "1":
        check_login.login()
    else:
        check_login.register()





