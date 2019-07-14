# coding:utf-8


def merge_sort(lists):
    """归并排序"""

    mid = len(lists)//2
    if mid<1:
        return lists

    lift_list = merge_sort(lists[:mid])
    right_list = merge_sort(lists[mid:])
    result = []
    lift = 0
    right = 0
    while lift<len(lift_list) and right <len(right_list):
        if lift_list[lift] <= right_list[right]:
            result.append(lift_list[lift])
            lift += 1
        else:
            result.append(right_list[right])
            right +=1

    result += lift_list[lift:]
    result += right_list[right:]

    return result


if __name__ == "__main__":
    import numpy as np
    import copy
    import time

    lists = np.random.randint(0, 100, 500000)
    lists = list(lists)

    list_n = len(lists)
    temp = copy.deepcopy(lists)
    start = time.clock()
    temp.sort(key=None, reverse=False)

    print(time.clock() - start)
    start = time.clock()

    result = merge_sort(lists)
    print(time.clock() - start)
