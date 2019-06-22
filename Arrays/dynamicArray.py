#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#
def dynamicArray(n, queries):
    overall_seq = [[] for l in range(n)]
    lastAnswer = 0
    output = []
    for query in queries:
        this_ind = ((query[1]^lastAnswer) % n)
        if(query[0]==1):
            overall_seq[this_ind].append(query[2])
        else:
            ans_index = query[2] % len(overall_seq[this_ind])
            lastAnswer = overall_seq[this_ind][ans_index]
            output.append(lastAnswer)
        print(overall_seq)
    return output

# Needed to catch that it was the VALUE of the ans_index that needed to be
# found and appended, not the ans_index itself (read questions more carefully!)
