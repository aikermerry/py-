import math

sum=0
num=10**21+1
for i in range(10**21,num):
    i=str(i)
    for m in range(0,21):
        sum+=int(i[m])
    if sum==int(i):
        print(sum)
