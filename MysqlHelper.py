# coding:utf-8
"""
@autor :aikermerry
简化mysql的使用
"""
from MySQLdb import *

class MysqlHelper(object):
    def __init__(self,host,user,passwd,db,port=3306,charset="utf8"):
        self.user = user
        self.passwd = passwd
        self.port = port
        self.host = host
        self.db = db
        self.charset = charset

    def connects(self):
        self.conn = connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db,
                           port=self.port,charset=self.charset)
        self.cur = self.conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()

    def cud(self,sql,params=[]):
        """数据库的增删改"""
        try:
            self.connects()
            self.cur.execute(sql,params)
            self.conn.commit()
            self.close()
            print("*******操作成功********")
        except Exception as e:
            print("出错")
            print(e)

    def find_get(self,sql,params=[]):
        """数据库的查询"""
        try:
            self.connects()
            self.cur.execute(sql,params)
            self.result = self.cur.fetchall()
            self.close()
            print("*******查询成功********")
            return self.result
        except Exception as e:
            print(e.args)
    def show_result(self):
        for i in self.result:
            print(i)






