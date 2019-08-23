"""新版教务系统模拟登录

See:http://jwc.xhu.edu.cn/xtgl/login_slogin.html

written by pengyao1207

        2019/8/23"""

import base64
import re
import requests
import rsa


def login(id, password):
    """登录

       @id:学号
       
       @password:密码
       348c31bf-6c15-4213-ab98-1b937bd12393
       返回session"""
    session = requests.Session()
    publickey = session.get(
        'http://jwc.xhu.edu.cn/xtgl/login_getPublicKey.html?').json()
    modulus = base64.b64decode(publickey['modulus'])
    exponent = base64.b64decode(publickey['exponent'])


    pubkey = rsa.PublicKey(int.from_bytes(modulus, 'big'),
                           int.from_bytes(exponent, 'big'))

    mm = base64.b64encode(rsa.encrypt(password.encode('utf-8'), pubkey))
    csrftoken = re.search(r"(name=\"csrftoken\" value=\")(.*?)(\"/>)", session.get(
        'http://jwc.xhu.edu.cn/xtgl/login_slogin.html').text).group(2)

    session.post('http://jwc.xhu.edu.cn/xtgl/login_slogin.html',
                 data={'csrftoken': csrftoken, 'yhm': id, 'mm': mm})
    return session


def getkb(session, year, mouth):
    """查课表
    
        @session
        
        @year:年份
        
        @mouth:月份，只能是3或者12
        
        返回一个json"""
    r = session.post(url='http://jwc.xhu.edu.cn/kbcx/xskbcx_cxXsKb.html?gnmkdm=N2151',
                     data={'xnm': str(year),  'xqm': str(mouth)})
    return r.json()


if __name__ == "__main__":
    
    id = ''  # 学号
    password = ''  # 密码
    session = login(id, password)  # 登录
    kb = getkb(session, 2019, 2)  # 获取课表,上半学期
    lists =['xqjmc','jc','kcmc','cdmc','zcd']
    kb_len = len(kb['kbList'])
    kb_list = [[kb['kbList'][x][i] for i in lists] for x in range(kb_len)]
    for x in kb_list:
    	print(x)


    