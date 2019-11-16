#!/bin/python3

import math
import os
import random
import re
import sys

def third_num(query):
    return query[2]

# Complete the arrayManipulation function below.
########### OLD #######################
# def arrayManipulation(n, queries):
#     total_added = {}
#     for query in queries:
#         a, b, k = query[0], query[1], query[2]
#         if(k==0):
#             continue
#         for element in range(a, b+1):
#             if(element in total_added):
#                 total_added[element] += k
#             else:
#                 total_added[element] = k
#
#     return max(total_added.values())

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    total_added = {}
    interval_arr = [0 for i in range(n)]
    max_val = 0
    curr_sum = 0
    for query in queries:
        start, end, k = query[0], query[1], query[2]
        if(k==0):
            continue
        interval_arr[start-1]+=k
        if(end<n):
            interval_arr[end]-=k

    for i in range(n):
        curr_sum+=interval_arr[i]
        if(curr_sum>max_val):
            max_val=curr_sum

    return max_val


print(arrayManipulation(4, [[2, 3, 603], [1, 1, 286], [4, 4, 882]]))

    # initial_arr = [0 for i in range(n)]
    # for query in queries:
    #     a, b, k = query[0], query[1], query[2]
    #     # initial_arr[a:b+1] = [l+k for l in initial_arr[a:b+1]]
    #     initial_arr[a:b+1] += k

#gives 24/60 points
# def arrayManipulation(n, queries):
#     total_added = {}
#     for query in queries:
#         a, b, k = query[0], query[1], query[2]
#         for element in range(a, b+1):
#             if(element in total_added):
#                 total_added[element] += k
#             else:
#                 total_added[element] = k
#
#     return max(total_added.values())

#work backwards from largest "k"
# total_added = {}
# max_K = sorted(queries, key=third_num, reverse=True)
# k_limit = sum(max_K[:][2])
# for query in max_K:
#     a, b, k = query[0], query[1], query[2]
#     for element in range(a, b+1):
#         if(element in total_added):
#             total_added[element] += k
#         else:
#             total_added[element] = k
