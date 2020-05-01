#!/bin/python3

import math
import os
import random
import re
import sys
import functools

# Complete the countSort function below.
def countSort(arr):
    firstHalf = len(arr)/2
    count_arr = [0 for i in range(100)]
    helper_arr = [[] for i in range(100)]
    for i, (val, chars) in enumerate(arr):
        val2 = int(val)
        count_arr[val2]+=1

        if(i<firstHalf):
            helper_arr[val2].append("-")
        else:
            helper_arr[val2].append(chars)

    print(*functools.reduce(lambda x,y: x+y, helper_arr), sep=" ")
