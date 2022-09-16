#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

class Node():
    def __init__(self):
        self.level = 0
        self.left = None
        self.right = None

def buildTree(arr):
    # build the binary digit tree for a single bucket here
    # using the input array of binary values

    # iterate over each binary number
    # adding nodes for each to the tree
    # until all numbers have been added

    root = Node()
    root.level = 1

    for i, binary_str in enumerate(arr):
        # print(binary_str)
        for j, val in enumerate(binary_str):
            if(j == 0):
                curr_node = root
                # print(curr_node.level)
                continue
            if(val == "0"):
                if(curr_node.left == None):
                    curr_node.left = Node()
                    curr_node.left.level = curr_node.level + 1
                curr_node = curr_node.left
            else:
                if(curr_node.right == None):
                    curr_node.right = Node()
                    curr_node.right.level = curr_node.level + 1
                curr_node = curr_node.right

    return root

# helper function
def findValStr(query_digit_str, curr_node):
    # find the complement given a digit from the query and the corresponding
    # node before it
    val_str = ""

    if(query_digit_str == "0"):
        if(not curr_node.right == None):
            val_str += "1"
            curr_node = curr_node.right
        else:
            val_str += "0"
            curr_node = curr_node.left
    else:
        if(not curr_node.left == None):
            val_str += "0"
            curr_node = curr_node.left
        else:
            val_str += "1"
            curr_node = curr_node.right

    return (val_str, curr_node)

# Complete the maxXor function below.
# Complete problem description available: https://www.hackerrank.com/challenges/maximum-xor/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=miscellaneous
def maxXor(arr, queries):
    non_dup_set = set(arr)
    reduced_arr = list(non_dup_set)
    reduced_arr.sort()
    zeroPresent = False
    largest_val = reduced_arr[-1]
    largest_val_bin = bin(largest_val).replace("0b", "")

    if(reduced_arr[0] == 0):
        zeroPresent = True
        reduced_arr.pop(0)

    # put into buckets by number of binary digits
    first_bucket_map = defaultdict(list)

    for val in reduced_arr:
        bucket = math.ceil(math.log2(val))
        first_bucket_map[bucket].append(bin(val).replace("0b", ""))

    # then make into trees
    bucket_sizes = sorted(list(first_bucket_map.keys()))
    bucket_size_set = set(bucket_sizes)
    max_bucket_size = bucket_sizes[-1]
    bucket_tree_map = {}

    for bucket in bucket_sizes:
        # should set the bucket size reference to the root for each of the bucket trees
        bucket_tree_map[bucket] = buildTree(first_bucket_map[bucket])

    # now find the best value to maximize the xor function with the query
    # and add to an array to be output
    output = []
    val_str = "1"

    for query in queries:
        if(query == 0):
            output.append(largest_val)
            continue

        # always pick the leftmost zero in the largest value (query or saved) to complement if possible (as the bucket)
        # otherwise pick zero if no zeros present in largest value (query or saved) or if no complements
        # otherwise pick the smallest number
        # case where query is zero - add largest value
        curr_largest_val = max(largest_val, query)

        query_bin = bin(query).replace("0b", "")
        query_bin_size = len(query_bin)

        # need to fit into query holes (if any)
        if(query_bin_size >= max_bucket_size):

            # find zeroes in curr_largest_val
            curr_largest_bin = bin(query).replace("0b", "")
            curr_largest_size = len(query_bin)
            zero_locs = [i for i in range(curr_largest_size) if (curr_largest_bin[i] == "0" and curr_largest_size - i in bucket_size_set)]

            # case where no buckets match
            if(len(zero_locs) == 0):
                if(zeroPresent):
                    output.append(query)
                    continue
                else:
                    #find complement to query in lowest bucket
                    smallest_bucket = bucket_sizes[0]
                    query_start_ind = curr_largest_size - smallest_bucket
                    val_str = "1"
                    curr_node = bucket_tree_map[smallest_bucket]
                    for i in range(smallest_bucket):
                        curr_query_digit = query_bin[query_start_ind + i]
                        next_val, curr_node = findValStr(curr_query_digit, curr_node)
                        val_str += next_val

            else:
                # add bucket that complements the query and starts by filling the leftmost zero
                # print(zero_locs)
                query_start_ind = zero_locs[0]
                best_bucket_size = curr_largest_size - zero_locs[0]
                val_str = "1"
                curr_node = bucket_tree_map[best_bucket_size]
                for i in range(best_bucket_size):
                    if(i == 0):
                        continue
                    curr_query_digit = query_bin[query_start_ind + i]
                    next_val, curr_node = findValStr(curr_query_digit, curr_node)
                    val_str += next_val

        # need to fit into largest bucket holes
        else:
            # find complement in largest bucket for query
            # use max bucket size because it has a 1 higher than anything in the query
            # and will therefore be higher
            val_str = "1"
            curr_node = bucket_tree_map[max_bucket_size]
            for i in range(1, max_bucket_size):
                if(curr_node == None):
                    break
                if(max_bucket_size - i > query_bin_size):
                    if(not curr_node.right == None):
                        val_str += "1"
                        curr_node = curr_node.right
                    else:
                        val_str += "1"
                        curr_node = curr_node.left
                else:
                    curr_query_digit = query_bin[query_bin_size + i - max_bucket_size]
                    next_val, curr_node = findValStr(curr_query_digit, curr_node)
                    val_str += next_val


        # add val_str to output as a decimal number xored with the query
        output.append(int(val_str, 2) ^ query)

    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    queries = []

    for _ in range(m):
        queries_item = int(input())
        queries.append(queries_item)

    result = maxXor(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
