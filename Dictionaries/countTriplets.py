#!/bin/python3

import math
import os
import random
import re
import sys
import numpy

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

# #helper function to count ones
# #not as efficient as just using a num choose 2 formula (combination)
# def countOnes(num):
#     total = 0
#     for i in range(1, num+1):
#         total+=(num-i)
#
#     return total

# Complete the countTriplets function below.
def countTriplets(arr, r):
    tripletCount = 0
    # need to examine original arr to know how many indexes are above
    # a certain value for the i<j<k requirement to hold
    arr = list(arr)
    arr2 = sorted(arr)
    seen = {}

    #need to use the original array to check indexes easier
    for i, first in enumerate(arr2):
        #first is the first of the possible triplets
        #breaks loop if no more pairs are possible
        second = first*r
        print(seen)
        if(second*r>arr2[-1]):
            break
        #search for the second value in array using binary search
        if(second not in seen):
            second_ind = binary_search_recursive(arr2, second, i, len(arr2)-1)
            if(second_ind!=-1):
                #put code here to only count this value above current index
                seen[second] = arr2.count(second)
                third = second*r
                third_ind = binary_search_recursive(arr2, third, i, len(arr2)-1) #can change the left edge of search here
                if(third_ind!=-1):
                    #put code here to only count this value above current index
                    seen[third] = arr2.count(third)
                    if(third!=first):
                        tripletCount+=seen[second]*seen[third]
                    else:
                        seen[second] -= 1
                        tripletCount+= (seen[second])*(seen[second]-1)/2
        else:
            third = second*r
            if(third not in seen):
                third_ind = binary_search_recursive(arr2, third, i, len(arr)-1) #can change the left edge of search here
                if(third_ind!=-1):
                    #put code here to only count this value above current index
                    seen[third] = arr2.count(third)
                    if(third!=first):
                        tripletCount+=seen[second]*seen[third]
                    else:
                        seen[second] -= 1
                        tripletCount+= (seen[second])*(seen[second]-1)/2
            else:
                if(third!=first):
                    tripletCount+=seen[second]*seen[third]
                else:
                    seen[second] -= 1
                    tripletCount+= (seen[second])*(seen[second]-1)/2

    print(seen)
    print(sum(seen.values()))
    print(len(arr))
    return int(tripletCount)

print(countTriplets(numpy.ones(100000), 1))

if __name__ == '__main__':
    f = open("countTripletsTest10.py", 'r')

    if f.mode == 'r':
        contents = f.read()

    f.close()

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, contents.rstrip().split()))

    ans = countTriplets(arr, r)

    print(ans)

    # fptr.write(str(ans) + '\n')
