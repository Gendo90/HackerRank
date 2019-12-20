#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    a.sort()
    b.sort()
    first_list = []
    #makes a list of all the numbers that
    #can be factored by a and are less than or equal to the minimum element of b
    #could make into another function when refactoring
    for item in range(a[-1], b[0]+1):
        valid = False
        for factor in a:
            if(item%factor==0):
                continue
            else:
                break
        else:
            valid=True
        if(valid):
            first_list.append(item)

    between_list = []
    for factor in first_list:
        valid = False
        for multiple in b:
            if(multiple%factor==0):
                continue
            else:
                break
        else:
            valid = True
        if(valid):
            between_list.append(factor)

    return len(between_list)
