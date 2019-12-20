#!/bin/python

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    #case where there are not enough squares to match the
    #birth month requirement
    if(m>len(s)):
        return 0

    sols = 0
    for i in range(0, len(s)-m+1):
        if(sum(s[i:i+m])==d):
            sols+=1

    return sols
