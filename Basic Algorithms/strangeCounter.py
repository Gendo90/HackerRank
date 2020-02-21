#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the strangeCounter function below.
def strangeCounter(t):
    #use a logarithm of base 2 to find out how many times it has doubled
    #but can use a while loop iteratively
    c=0
    while(3*(2**(c)) < t):
        t-=3*(2**(c))
        c+=1

    #maximum value of timer for this cycle
    max_count = 3*(2**(c))
    
    #finally, subtract remainder of t from 3*(2^(c+1))
    return max_count-(t-1)


print(strangeCounter(4))
print(strangeCounter(8))
print(strangeCounter(14))
