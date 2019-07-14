# coding:utf-8
import  time
def select_sort(lists):

    n = len(lists)
    for m in range(n-1):
        min_num = m
        for i in range(m,n):
            if lists[min_num] > lists[i]:
                min_num = i
        lists[m],lists[min_num] = lists[min_num],lists[m]


if __name__ == "__main__":
    # lists = [1,2,4,4,3,3,2,3,44,5,5,3,22,2,23,56,4,33,78,0,554,23,12,23,45,67,89,90,87,65,43,22,123]
    import numpy as np
    lists = np.random.randint(0, 100, 500)
    lists = lists.tolist()
    temp = lists
    start = time.clock()
    temp.sort(key=None, reverse=False)
    print(temp)
    print(time.clock() - start)
    start = time.clock()

    select_sort(lists)
    print(lists)
    print(time.clock() - start)
