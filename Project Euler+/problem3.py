#!/bin/python3

import math
import os
import random
import re
import sys

# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

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

#maxvalue
def largestPrimeFactor(num):
    reduced = num
    check = 2
    factors = []
    primeFactors = []
    while(check<int(math.sqrt(num))+2):
        if(reduced/check == round(reduced/check)):
            print(check, reduced)
            reduced /= check
            factors.append(check)
            if(isPrimeUpgraded(check)):
                primeFactors.append(check)
        check+=1
        print(check)

    print(factors)
    return factors, primeFactors

# print(largestPrimeFactor(13195))
print(largestPrimeFactor(600851475143))


#returns 4613732 - correct!
