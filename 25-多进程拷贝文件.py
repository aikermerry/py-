import os
from multiprocessing import Manager ,Pool


oldFileName = input("请输入需要复制的文件夹:")

newFileName = input("请输入新文件夹名字:")

os.mkdir(newFileName )

def copyFile(name,oldFileName,newFileName,q):
    qr = open(oldFileName+"/"+name,"r")
    qw = open(newFileName+"/"+name,"w+")
    coment = qr.read()
    qw.write(coment)
    qw.close()
    qr.close()
    q.put(name)
def main():
    pool = Pool(5)
    q = Manager().Queue()

    fileNames = os.listdir(oldFileName)

    for name in fileNames:
        pool.apply_async(copyFile,args=(name,oldFileName,newFileName,q))
    num = 0
    while num<len(fileNames):
        q.get()
        num+=1
        print("\r复制进度 %.2f%%" %((num/len(fileNames))*100),end="")
    pool.close()
    pool.join()
    print("\n完成")

if __name__ == "__main__":
    main()
