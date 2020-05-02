#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    min_root = math.sqrt(a)
    max_root = math.sqrt(b)

    #find the integer values of the min and max roots
    if(int(min_root)!=min_root):
        min_root = int(min_root+1)

    if(int(max_root)!=max_root):
        max_root = int(max_root)

    return int(max_root-min_root+1)


print(squares(26, 27))
print(squares(16, 36))
