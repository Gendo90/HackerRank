#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    elevation = 0
    total_valleys = 0
    for step in s:
        if(step=="D" and elevation==0):
            elevation -= 1
            total_valleys+=1
        elif(step=="D"):
            elevation-=1
        else:
            elevation +=1
    return total_valleys


print(countingValleys(8, "UDDDUDUU"))
