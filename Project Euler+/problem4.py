#!/bin/python3

import math
import os
import random
import re
import sys

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def largestPalindromeProduct3Digits():
    largestPalProduct = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            test = str(i*j)
            if(test == test[::-1] and int(test)>largestPalProduct):
                largestPalProduct = int(test)

    return largestPalProduct


print(largestPalindromeProduct3Digits())


#returns 4613732 - correct!
