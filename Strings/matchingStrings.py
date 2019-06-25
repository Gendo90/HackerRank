#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
# NOTE: Not optimized, could probably run faster if each string is placed
# in a hash map and counted, and then see which queries match strings in the
# hash map for O(n) running time, but O(n) space complexity, too
def matchingStrings(strings, queries):
    output = []
    for item in queries:
        total_num = strings.count(item)
        output.append(total_num)

    return output

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     strings_count = int(input())
#
#     strings = []
#
#     for _ in range(strings_count):
#         strings_item = input()
#         strings.append(strings_item)
#
#     queries_count = int(input())
#
#     queries = []
