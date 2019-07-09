# coding:utf-8


class Node(object):
    """创建节点"""
    def __init__(self,data):
        self.data = data
        self.next = None


class SingleList(object):
    """创建链表"""
    def __init__(self,data=None):
        if data:
            nodes = Node(data)
            self.p = nodes
    #添加节点
    def add(self,data):
        nodes = Node(data)
        nodes.next = self.p
        self.p = nodes
    #插入节点
    def insert(self,location,data):
        nodes = Node(data)
        num = 1
        cur = self.p
        pre = self.p
        if num > location:
            nodes.next = self.p
            self.p = nodes
            return 0
        while cur:
            if num == location:
                nodes.next = cur
                pre.next = nodes
                if num ==1:
                    self.p = pre
                return 0
            if not cur.next:
                cur.next = nodes
                return 0
            pre =cur
            cur = cur.next
            num += 1
    #显示链表
    def show_list(self):
        cur = self.p
        while cur:
            print(cur.data,end=" ")
            if not cur.next:
                print("")
                return 0
            cur = cur.next
        print("data:None")
    #尾部添加节点
    def append(self,data):
        nodes = Node(data)
        cur = self.p
        while cur:
            if not cur.next:
                cur.next = nodes
                break
            cur = cur.next
    #链表长度
    def len_list(self):
        cur = self.p
        num = 0
        while cur:
            cur = cur.next
            num+=1
        return num
    #移除节点
    def remove(self,data):
        cur = self.p
        pre = self.p
        while cur:
            if cur.data == data:
                pre.next = cur.next
                if pre == self.p:
                    self.p = cur.next
                return 0
            pre = cur
            cur = cur.next
        print("Place check")


if __name__ == "__main__":
    singe_list = SingleList(100)
    singe_list.add(20)
    singe_list.add(30)
    singe_list.add(40)
    singe_list.append(50)
    singe_list.append(58)
    singe_list.show_list()
    singe_list.insert(4,24)
    singe_list.insert(-1,24)
    singe_list.show_list()
    singe_list.remove(24)
    singe_list.show_list()
    print(singe_list.len_list())
















