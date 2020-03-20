#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr.sort()
    minDiff = abs(arr[1]-arr[0])

    for i in range(len(arr)-1):
        diff = abs(arr[i+1]-arr[i])
        if(minDiff>diff):
            minDiff = diff

    return minDiff


print(minimumAbsoluteDifference([1, -3, 71, 68, 17]))
