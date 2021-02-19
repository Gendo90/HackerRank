#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the absolutePermutation function below.
def absolutePermutation(n, k):
    #base case for k=0:
    if(k==0):
        return [a for a in range(1, n+1)]

    perm_arr = [-1 for a in range(1, n+1)]
    unused = {}

    for i in range(1, n+1):
        unused[i] = True

    #populate the values from the beginning
    #through the end based on previous selections
    for i in range(1, n+1, 2*k):
        perm_arr[i-1] = k+i
        if(k+i not in unused):
            return [-1]
        else:
            unused.pop(k+i)

    #populate the values from the end through the beginning
    #based on the last value
    for i in range(n, 0, -2*k):
        perm_arr[i-1] = i-k
        if(i-k not in unused):
            return [-1]
        else:
            unused.pop(i-k)

    #check all leftover values
    for i in range(1, n+1):
        if(perm_arr[i-1] != -1):
            continue
        #pick which value is in the unused values
        #otherwise if not in unused values,
        #no solutions
        if(i-k in unused):
            perm_arr[i-1] = i-k
            unused.pop(i-k)
        elif(k+i in unused):
            perm_arr[i-1] = k+i
            unused.pop(k+i)
        else:
            return [-1]

    #might still be some values in between that are not used

    if(len(unused) != 0):
        return [-1]

    return perm_arr


print(absolutePermutation(6, 1))
