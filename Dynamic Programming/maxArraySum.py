#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.

#try to use the robHouses algorithm from AT&T interview - looks similar!
#not completely right, though...
def maxSubsetSum(arr):
    """Used dynamic programming to get solution, similar to knapsack problem"""

    maxAtHouse = [arr[0], max(arr[1], arr[0])]
    for i in range(2, len(arr)):
        maxAtHouse.append(max(maxAtHouse[i-2]+arr[i], maxAtHouse[i-1]))

    print(maxAtHouse)
    return maxAtHouse[-1]


def maxSubsetSum2(arr):
    """Used dynamic programming to get solution, similar to knapsack problem"""

    #note - need to allow a 0 to be at any point in the array!
    maxAtHouse = [max(0, arr[0]), max(arr[1], arr[0])]
    for i in range(2, len(arr)):
        #need to allow no choice here!
        maxAtHouse.append(max(maxAtHouse[i-2]+arr[i], maxAtHouse[i-1], maxAtHouse[i-2]))

    return maxAtHouse[-1]

arr = [-2, 1, 3, -4, 5]
print(maxSubsetSum(arr))
print(maxSubsetSum2(arr))
