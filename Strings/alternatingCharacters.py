#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    count = 0
    curr = s[0]
    for item in s:
        #flips the value
        if(item==curr):
            if(item=="A"):
                curr="B"
            else:
                curr="A"
        else:
            count+=1
    return count
