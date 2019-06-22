#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    num_swaps = 0
    for i in range(1, len(a)+1):
        for j in range(0, len(a)-i):
            if(a[j]>a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
                num_swaps+=1

    print("Array is sorted in {} swaps.".format(num_swaps))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[-1]))
