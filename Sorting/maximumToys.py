#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices.sort()
    count = 0
    while(k>=prices[0]):
        k-=prices.pop(0)
        count+=1

    return count
