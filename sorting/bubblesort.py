import random
import sys

sys.setrecursionlimit(100000)

def recursive_bubble_sort(list_):
    updated = False

    for idx in range(0, len(list_)-1):
        if list_[idx] > list_[idx+1]:
            list_[idx], list_[idx+1] = list_[idx+1], list_[idx]
            updated = True

    if updated:
        recursive_bubble_sort(list_)
    return list_


def looping_bubble_sort(list_):
    updated = True
    while updated:
        updated = False
        for idx in range(0, len(list_)-1):
            if list_[idx] > list_[idx+1]:
                list_[idx], list_[idx+1] = list_[idx+1], list_[idx]
                updated = True
    return list_

if __name__ == '__main__':
    out_list = looping_bubble_sort([random.randrange(0, 1000000000) for _ in range(0, 10000)])
    print 'sorted {0} length list'.format(len(out_list))
