#!/bin/python3

import math
import os
import random
import re
import sys

#EASY to make work, but HARD to get input/output correct!

# Complete the maxElement function below.
def maxElement(s):
    this_stack = []
    this_max = 0
    for query in s:
        if(query[0]==1):
            this_stack.append(query[1])
            if(query[1]>this_max):
                this_max=query[1]
        elif(query[0]==2):
            l = this_stack.pop()
            if(l==this_max):
                try:
                    this_max = max(this_stack)
                except ValueError:
                    this_max = 0
        else:
            print(this_max)



n = int(input())

total_arr = []
for i in range(n):
    arr = input()
    if(len(arr)>1):
        arr = arr.split(" ")
        arr = [int(a) for a in arr]
    else:
        arr = [int(a) for a in arr]
    total_arr.append(arr)

maxElement(total_arr)
