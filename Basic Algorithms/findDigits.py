#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    digits = [int(a) for a in (str(n))]
    divisorCount = 0
    for digit in digits:
        if(digit==0):
            continue
        if(n%digit==0):
            divisorCount+=1

    return divisorCount



print(findDigits(1012))
