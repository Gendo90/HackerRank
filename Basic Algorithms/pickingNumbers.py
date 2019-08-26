#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    #initialize a hash map to store the frequency of each value seen
    seen_vals = {}
    for num in a:
        if(num in seen_vals):
            seen_vals[num]+=1
        else:
            seen_vals[num] = 1

    max_size = 0
    for item in seen_vals.keys():
        num_for_item = seen_vals[item]
        if(seen_vals.get(item+1)):
            plus_one = seen_vals.get(item+1)
        else:
            plus_one = 0

        if(max_size<(num_for_item+plus_one)):
            max_size = num_for_item+plus_one

    return max_size

arr = [1, 1, 2, 2, 4, 4, 5, 5, 5]

print(pickingNumbers(arr))
