#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(h):
    max_area = 0
    total_buildings = len(h)
    for i, current_bldg in enumerate(h):
        current_width = 1
        j=i+1
        #first look forwards from this point in the array
        while(j<total_buildings and h[j]>=current_bldg):
            current_width+=1
            j+=1

        l = i-1
        #then look backwards for greater or equal heights!
        while(0<=l and h[l]>=current_bldg):
            current_width+=1
            l-=1

        this_area = current_width*current_bldg
        # print(current_bldg, this_area, max_area)
        if(this_area>max_area):
            max_area=this_area

    return max_area


print(largestRectangle([11, 11, 10, 10, 10]))
