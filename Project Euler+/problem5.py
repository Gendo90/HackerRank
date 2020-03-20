#!/bin/python3

import math
import os
import random
import re
import sys
import functools


def isPrimeUpgraded(n):
    """A prime checker function - determines if n is prime faster O(sqrt(n))
    time"""

    if(not isinstance(n, int)):
        return False

    #special cases
    if(n==2):
        return True
    if(n<2):
        return False

    for i in range(2, int(math.sqrt(n))+2):
        if(n%i==0):
            return False

    return True

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def allDivide(num, startVal=1):
    factors = []
    for i in range(1, num+1):
        if(isPrimeUpgraded(i)):
            factors.append(i)
        else:
            test = i
            for item in factors:
                if(test/item == round(test/item)):
                    test /= item
                if(test == 1):
                    break
            else:
                factors.append(test)

    print(factors)
    return functools.reduce(lambda x, y: x*y, factors)


print(allDivide(20))
#232792560 ->




#returns 4613732 - correct!
