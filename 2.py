import socket
import threading
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.11.58",9999))  # 使用connect方法连接服务器
true=True
def rec(s):
    global true
    while true:
        t=s.recv(1024).decode("utf8")  #客户端也同理
        if t == "exit":
            true=False
        print(t)
trd=threading._start_new_thread(target=rec,args=(s,))
trd.start()
while true:
    t=input()
    s.send(t.encode('utf8'))
    if t == "exit":
        true=False
s.close()
