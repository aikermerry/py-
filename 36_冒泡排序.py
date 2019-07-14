# coding:utf-8
import time

def double_sort(lists):
    for n in range(len(lists)-1):
        for i in range(len(lists)-1-n):
            """内层循环"""
            if lists[i] > lists[i+1]:
                lists[i],lists[i+1] = lists[i+1],lists[i]




if __name__ == "__main__":
    import copy
    import numpy as np
    lists =  np.random.randint(0, 100, 500)
    lists = list(lists)
    temp = copy.deepcopy(lists)
    start = time.clock()
    temp.sort()
    print(time.clock() - start)


    start = time.clock()

    double_sort(lists)

    print(time.clock() - start)
