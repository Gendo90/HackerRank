#!/bin/python3

import math
import os
import random
import re
import sys

#helper function to merge the separate arrays
def merge_and_count_split_inv(left, right):
    inv = 0
    i=0
    j=0
    output_arr = []

    while(len(output_arr)<(len(left)+len(right))):
        if(left[i]<=right[j]):
            output_arr.append(left[i])
            i+=1
        else:
            output_arr.append(right[j])
            j+=1
            inv+=len(left[i:])
        if(i==len(left)):
            output_arr.extend(right[j:])
        elif(j==len(right)):
            output_arr.extend(left[i:])


    return inv, output_arr

# Complete the countInversions function below.
def countInversions(arr):
    if(len(arr)==1):
        return 0, arr

    middle = len(arr)//2
    left = arr[:middle]
    right = arr[middle:]

    (x, sorted_left) = countInversions(left)
    (y, sorted_right) = countInversions(right)
    (z, merged) = merge_and_count_split_inv(sorted_left, sorted_right)

    return x+y+z, merged


arr = [2, 1, 3, 1, 2]

print(countInversions(arr))
