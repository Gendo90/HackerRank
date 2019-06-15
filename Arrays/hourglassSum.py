#!/bin/python3

import math
import os
import random
import re
import sys

#helper function to calculate the sum of an hourglass
def hourglassCalc(i, j, m):
    total = 0
    total+=sum(m[i][v] for v in range(j, j+3))
    total+=m[i+1][j+1]
    total+=sum(m[i+2][v] for v in range(j, j+3))
    return total


# Complete the hourglassSum function below.
def hourglassSum(arr):
    hourglassTotals = [hourglassCalc(i, j, arr) for i in range(0, len(arr[0])-2) for j in range(0, len(arr)-2)]
    return max(hourglassTotals)

print(hourglassSum([[1, 2, 3], [3, 4, 5], [6, 7, 8]]))
