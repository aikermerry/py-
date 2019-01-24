class Itcast(object):
    def __init__(self,subject1):
        self.subject1 = subject1
        self.subject2 = 'cpp'
    def __getattribute__(self,obj):
        if obj == 'subject1':
            print('log subject1')
           # return 'redirect python'
        #else: #测试时注释掉这2⾏， 将找不到subject2
        return object.__getattribute__(self,obj)
    def show(self):
        print('this is Itcast')

s = Itcast("python")
print(s.subject1)
print(s.subject2)