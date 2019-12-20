#!/bin/python

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    min_start = min(x1, x2)
    max_start = max(x1, x2)
    min_vel = min(v1, v2)
    max_vel = max(v1, v2)
    #case where they start at the same position
    if(x1==x2):
        return "YES"
    #case where the slower kangaroo starts behind the faster one and
    #can never catch up
    if((min_start==x1 and min_vel==v1)
        or (min_start==x2 and min_vel==v2)):
        return "NO"

    #check each hop to see if the kangaroos meet, and stop checking when the
    #faster one moves past the slower one
    while(min_start<=max_start):
        if(min_start==max_start):
            return "YES"
        min_start+=max_vel
        max_start+=min_vel

    return "NO"
