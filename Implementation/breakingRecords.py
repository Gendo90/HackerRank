#!/bin/python

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    min_record = scores[0]
    max_record = scores[0]
    min_broken_count = 0
    max_broken_count = 0

    for score in scores[1:]:
        if score<min_record:
            min_broken_count+=1
            min_record = score
        if score>max_record:
            max_broken_count+=1
            max_record = score

    return max_broken_count, min_broken_count
