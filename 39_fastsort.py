# coding:utf-8
import time


def fast_sort(lists,first,last):

    if first >= last:
        return 0
    low = first
    high = last
    value = lists[low]

    while low < high:
        #从高位开始移动
        while lists[high] >= value and high > low:
            high -= 1
        lists[low] = lists[high]
        #从低位开始移动
        while lists[low] < value and high > low:
            low += 1
        lists[high] = lists[low]
    #当高低指针相等时，开始
    lists[low] = value
    #递归排列其他中间值两端的部分
    fast_sort(lists,first,low-1)
    fast_sort(lists,high+1 , last)


if __name__ == "__main__":
    import numpy as np
    import copy
    lists = np.random.randint(0,100,500000)
    lists = list(lists)
    list_n = len(lists)
    temp = copy.deepcopy(lists)
    start = time.clock()
    temp.sort(key=None, reverse=False)

    print(time.clock() - start)
    start = time.clock()

    fast_sort(lists,0,list_n-1)
    print(time.clock() - start)
