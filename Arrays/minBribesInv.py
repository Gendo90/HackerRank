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
def minimumBribes(arr, first_time=True):
    if(first_time):
        for i, item in enumerate(arr):
            if(item>i+3):
                return "Too chaotic", None

    arr_len = len(arr)
    if(arr_len==1):
        return 0, arr

    middle = arr_len//2
    left = arr[:middle]
    right = arr[middle:]

    (x, sorted_left) = minimumBribes(left, first_time=False)
    (y, sorted_right) = minimumBribes(right, first_time=False)
    (z, merged) = merge_and_count_split_inv(sorted_left, sorted_right)

    return x+y+z, merged


arr = [2, 1, 5, 3, 4]
arr2 = [2, 5, 1, 3, 4]

print(minimumBribes(arr)[0])
print(minimumBribes(arr2)[0])
