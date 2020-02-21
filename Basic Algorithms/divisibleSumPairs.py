#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    #straightforward solution might work, O(n^2) time
    num_pairs = 0

    for i, val in enumerate(ar):
        for second_val in ar[i+1:]:
            if((val+second_val)%k==0):
                num_pairs+=1

        if(i==len(ar)-2):
            break

    return num_pairs


print(divisibleSumPairs(6, 3, [1,3,2,6,1,2]))
