## 读取mat文件

导入模块：import scipy.io as scio 

 dataFile  = "绝对路径" 

data = scio.loadmat(dataFile)



注意data 的格式为字典



### 保存文件



dataName = "./dataNew.mat"

scio.savemat(dataName,{"A":list[A]})



