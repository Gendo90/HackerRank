#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY skillLevel
#  2. INTEGER minDiff
#

def maxPairs(skillLevel, minDiff):
    #first sort the array
    skillLevel.sort()
    print(skillLevel)

    #find the highest value (start index -1) and the first paired value
    size = len(skillLevel)
    max_ind = 1
    first_min = 0
    while(max_ind<size and skillLevel[max_ind]-skillLevel[first_min]<minDiff):
        max_ind+=1

    #otherwise, couple up the students and reduce the left and right indices as required
    right_ind = max_ind
    left_ind = 0
    total_pairs = 0
    matched_indices = set()

    while(right_ind<size):
        if(right_ind==left_ind):
            right_ind+=1
            continue
        if(skillLevel[right_ind] - skillLevel[left_ind] >=minDiff):
            if(left_ind in matched_indices):
                left_ind+=1
                continue
            if(right_ind in matched_indices):
                right_ind+=1
                continue
            matched_indices.add(right_ind)
            matched_indices.add(left_ind)
            print(left_ind, right_ind)
            total_pairs+=1
            right_ind-=1
        right_ind+=1

    return total_pairs


# print(maxPairs([58938146, 219080001, 290589043, 306989605, 318554335, 345194195, 376420327, 509674780, 802573599, 939226418], 22586934))
# #result should be 5
# #need to go backwards? still does not work for some test cases
# print(maxPairs([25107191, 123232501, 151290765, 183012194, 473251358, 579542802, 689345248, 709552565, 803612259, 862726097, 994391793], 440987423))
# #result should be 5
# print(maxPairs([3, 4, 5, 2, 1, 1], 3))
#result should be 2

#do some kind of binary search for value, to find closest value to difference?
#Use some kind of dynamic programming? Sets of numbers greater than this one by the difference? E.g. for backwards case, only one number greater than the 473251358,
#must be used in that pair?

#dynamic programming - solution is to find the number of different min indexes for working values that are present in the array


#modified to return index where the item would be!
def binary_search_recursive(a, x, left, right):

    index = (left+right)//2
    if a[index]==x:
        return index
    elif x>(a[right]) or x<a[left]: # first case where x is not in the list!
        if(x>a[right]):
            return right+1
        else:
            return left
    elif left==right: # case where search is complete and no value x not found
        return left
    elif left==right-1: # case where there are only two numbers left, check both!
        left = right
        return binary_search_recursive(a, x, left, right)
    elif a[index]<x:
        left = index
        return binary_search_recursive(a, x, left, right)
    elif a[index]>x:
        right = index
        return binary_search_recursive(a, x, left, right)

def experimentMaxPairs(skillLevel, minDiff):
    #first sort the array
    skillLevel.sort()

    size = len(skillLevel)
    left_ind = 1
    currMin = binary_search_recursive(skillLevel, skillLevel[0]+minDiff, 0, size-1)
    minInd = {0:currMin}

    print(skillLevel)

    while(left_ind<size):
        if(currMin>=size):
            break
        #perform a binary search here for each number + min diff, to fill out map
        minInd[left_ind] = binary_search_recursive(skillLevel, skillLevel[left_ind]+minDiff, 0, size-1)
        if(minInd[left_ind]<=currMin):
            minInd[left_ind]+=1
        currMin = minInd[left_ind]

        left_ind+=1

    print(minInd)

    result = set(minInd.values())
    # result.discard(-1)

    return min(len(result)-1, size//2)

print(experimentMaxPairs([58938146, 219080001, 290589043, 306989605, 318554335, 345194195, 376420327, 509674780, 802573599, 939226418], 22586934))
#need to go backwards? still does not work for some test cases
print(experimentMaxPairs([25107191, 123232501, 151290765, 183012194, 473251358, 579542802, 689345248, 709552565, 803612259, 862726097, 994391793], 440987423))
print(experimentMaxPairs([3, 4, 5, 2, 1, 1], 3))
print(experimentMaxPairs([1, 1, 1, 1], 4))
