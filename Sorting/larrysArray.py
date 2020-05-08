#!/bin/python3

import math
import os
import random
import re
import sys

def rotate(arr):
    arr[0], arr[1], arr[2] = arr[1], arr[2], arr[0]
    return arr

# Complete the larrysArray function below.
def larrysArray(A):
    size_A = len(A)

    for i in range(1, size_A+1):
        # print(A, i)
        if(A[i-1]==i):
            continue

        curr_ind = A.index(i)
        #case where the value has been rotated below where it should be, cannot
        #be sorted this way!
        if(curr_ind<i):
            break
        else: #case where the value must be rotated down!
            moved_ind = curr_ind
            while(moved_ind>i-1):
                rot_count = 0
                inner_break = False
                while(rot_count<2 and A[i-1] != i):
                    if(moved_ind-2 < 0 or A[moved_ind-2]==i-1):
                        if(moved_ind+2>size_A):
                            inner_break = True
                            break
                        A[moved_ind-1:moved_ind+2] = rotate(A[moved_ind-1:moved_ind+2])
                    else:
                        if(moved_ind+1>size_A):
                            inner_break = True
                            break
                        A[moved_ind-2:moved_ind+1] = rotate(A[moved_ind-2:moved_ind+1])
                    rot_count+=1
                if(inner_break):
                    break
                moved_ind-=rot_count
    else:
        return "YES"

    return "NO"

print(larrysArray([1, 6, 5, 2, 4, 3]))
print(larrysArray([1, 6, 5, 2, 3, 4]))
print(larrysArray([3, 1, 2, 4]))
