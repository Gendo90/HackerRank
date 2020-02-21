#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    height = 0
    for i in range(n+1):
        if(i%2==0):
            height+=1
        else:
            height*=2

    return height


print(utopianTree(3))
print(utopianTree(4))
