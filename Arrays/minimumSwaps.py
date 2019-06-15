#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    check_arr = sorted(arr)
    i=0
    total_swaps = 0
    while(arr!=check_arr):
        if(arr[i]!=check_arr[i]):
            item_ind = arr.index(check_arr[i])
            arr[i], arr[item_ind] = arr[item_ind], arr[i]
            total_swaps+=1
        i+=1
    return total_swaps

print(minimumSwaps([1, 3, 5, 2, 4, 6, 7]))
