#!/bin/python3

import math
import os
import random
import re
import sys

#helper function from algorithms class:
def binary_search_recursive(a, x, left, right):

    index = (left+right)//2
    if a[index]==x:
        return index
    elif x>(a[right]) or x<a[left]: # first case where x is not in the list!
        return -1
    elif left==right: # case where search is complete and no value x not found
        return -1
    elif left==right-1: # case where there are only two numbers left, check both!
        left = right
        return binary_search_recursive(a, x, left, right)
    elif a[index]<x:
        left = index
        return binary_search_recursive(a, x, left, right)
    elif a[index]>x:
        right = index
        return binary_search_recursive(a, x, left, right)

# Complete the minimumSwaps function below.
# must be a faster solution using quicksort or something else?
# count how many are out of order, then figure out how to solve
def minimumSwaps(arr):
    check_arr = sorted(arr)
    total_swaps = 0
    i=0
    misfit_arr = [a for i, a in enumerate(arr) if(arr[i]!=check_arr[i])]
    check_misfit_arr = sorted(misfit_arr)
    fixed_indexes = {}
    while(misfit_arr!=check_misfit_arr):
        if(misfit_arr[i]!=check_misfit_arr[i]):
            item_ind = binary_search_recursive(check_misfit_arr, misfit_arr[i], 0, len(check_misfit_arr)-1) # change to binary search to get log time here
            misfit_arr[i], misfit_arr[item_ind] = misfit_arr[item_ind], misfit_arr[i]
            total_swaps+=1
            fixed_indexes[item_ind] = True
        while(i+1 in fixed_indexes): # check against hashmap to aviod redundancy
            i+=1
        else:
            i+=1
        if(i==len(check_misfit_arr)):
            i=0
    return total_swaps

print(minimumSwaps([7, 1, 3, 2, 4, 5, 6]))

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)
    print(res)

    # fptr.write(str(res) + '\n')
    #
    # fptr.close()
