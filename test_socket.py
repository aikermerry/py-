import socket
import threading
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("0.0.0.0",9999)) ## 0,0,0,0的意思是所有ip都可以连接，后面的9999是端口。
s.listen(5)  ##这个是socket的监听事件，用来约束连接数量
sock,addr =s.accept()  #因为这个方法返回的是元组有两位，所以我直接使用两个接收。
print("有人连接！！")
print(sock)  #这里可以发现sock是网络用户的详细信息
print(addr) # 这个是连接网络的ip和端口
true=True
def rec(sock):
    global true
    while true:
        t=sock.recv(1024).decode('utf8')  #函数的核心语句就一条接收方法recv限制接收信息的大小使用byte单位。
        if t == "exit": #如果输入exit退出
            true=False
        print(t)
trd=threading._start_new_thread(target=rec,args=(sock,))  #使用_start_new_thread方法定义线程并执行，args这里必须使用元组所以有逗号。
while true:    #发送消息
    t=input()
    sock.send(t.encode('utf8'))  #使用socket的send方法发送消息无限循环
    if t == "exit":
        true=False
s.close()
