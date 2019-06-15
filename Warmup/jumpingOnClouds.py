#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    # greedy algorithm, try to take a step of 2 if possible, otherwise take
    # a step of 1
    i = 0
    total_jumps = 0
    while(i<len(c)-1):
        try:
            if(c[i+2]==1):
                i+=1
            else:
                i+=2
        except IndexError:
            i=len(c)-1
        total_jumps+=1
    return total_jumps


print(jumpingOnClouds([0, 0, 0, 1, 0, 0]))
