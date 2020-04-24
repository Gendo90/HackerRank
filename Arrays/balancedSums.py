#!/bin/python

import math
import os
import random
import re
import sys

# Complete the balancedSums function below.
def balancedSums(arr):
    #find the total of the array
    right_total = sum(arr)
    left_total = 0

    #loop over array, looking at the difference to the total
    for i, num in enumerate(arr):
        #reduce the right total by the current number
        right_total -= num
        #check if the right total equals the left total
        if(left_total==right_total):
            return "YES"
        #add the current number to the left total
        left_total+=num

    return "NO"


print(balancedSums([1, 2, 3]))
print(balancedSums([1, 2, 3, 3]))
