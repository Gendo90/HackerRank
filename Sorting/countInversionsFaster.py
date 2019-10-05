#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np
import time

#helper function to merge the separate arrays
def merge_and_count_split_inv(left, right):
    inv = 0
    i=0
    j=0
    left_len = len(left)
    right_len = len(right)
    output_arr = [0]*(left_len+right_len)

    while((i+j)<(left_len+right_len)):
        if(left[i]<=right[j]):
            output_arr[i+j] = left[i]
            i+=1
        else:
            output_arr[i+j] = right[j]
            j+=1
            inv+=left_len-i
        if(i==left_len):
            output_arr[i+j:]=(right[j:])
            break
        elif(j==right_len):
            output_arr[i+j:]=(left[i:])
            break


    return inv, output_arr

# Complete the countInversions function below.
def countInversions(arr):
    arr_len = len(arr)
    if(arr_len==1):
        return 0, arr

    middle = arr_len//2
    left = arr[:middle]
    right = arr[middle:]

    (x, sorted_left) = countInversions(left)
    (y, sorted_right) = countInversions(right)
    (z, merged) = merge_and_count_split_inv(sorted_left, sorted_right)

    return x+y+z, merged


arr = [2, 1, 3, 1, 2]

print(countInversions(arr))


if __name__ == '__main__':
    sys.setrecursionlimit(2000)
    n = 15

    d = 100000

    # arr = np.genfromtxt(r'inversions.txt', delimiter='/n')
    with open('inversions.txt') as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    # content = [x.strip() for x in content]

    arr = list(map(int, content[2].split(" ")))

    # print(arr)
    t0 = time.clock()
    result, output_arr = countInversions(arr)
    print(time.clock()-t0)

    print(result)
