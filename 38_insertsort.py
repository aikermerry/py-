# coding:utf-8
import timeit
import time
def insert_sort(lists):
    n = len(lists)
    for m in range(1,n):
        for i in range(m-1,-1,-1):
            if lists[m] < lists[i]:
                lists[m],lists[i] = lists[i],lists[m]
                m = i
            else:
                break


if __name__ == "__main__":
    import numpy as np
    import copy
    lists = np.random.randint(0, 100, 50000)
    lists = lists.tolist()
    temp = copy.deepcopy(lists)
    start = time.clock()
    temp.sort(key=None, reverse=False)

    print(time.clock() - start)
    start = time.clock()

    insert_sort(lists)

    print(time.clock() - start)




