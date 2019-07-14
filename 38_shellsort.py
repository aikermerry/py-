# coding:utf-8
import time
'''
希尔排序：
最坏时间复杂度 O（n^2）
最优时间复杂度 O(n^1.3)

'''


def shell_sort(lists):
    lists_n = len(lists)
    sap = lists_n//2
    while sap > 0:
        for i in range(sap,lists_n):
            while i >0:
                if lists[i] < lists[i-sap]:
                    lists[i],lists[i-sap] = lists[i-sap],lists[i]
                i -= sap
        sap //= 2


if __name__ == "__main__":
    # lists = [1,2,4,4,3,3,2,3,44,5,5,3,22,2,23,56,4,33,78,0,554,23,12,23,45,67,89,90,87,65,43,22,123]

    import numpy as np
    import copy
    lists = np.random.randint(0, 100, 500)
    lists = list(lists)
    start = time.clock()
    temp = copy.deepcopy(lists)
    temp.sort(key=None, reverse=False)
    print(temp)
    print(lists)
    print(time.clock() - start)
    start = time.clock()

    shell_sort(lists)
    print(lists)
    print(time.clock() - start)


