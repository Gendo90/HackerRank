#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    total = 0
    colors_seen = {}
    for color in ar:
        if(color not in colors_seen.keys()):
            total += ar.count(color)//2
            colors_seen[color] = True;
    return total


print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
