#!/bin/python3

import math
import os
import random
import re
import sys

#helper function binary search - replaces getIndex()
def binary_search_recursive(a, x, left, right):

    index = (left+right)//2
    if a[index]==x:
        return index
    elif x>(a[right]) or x<a[left]: # first case where x is not in the list!
        if(x>a[right]):
            return right+1
        else:
            return left-1
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

#helper function median()
def median(arr, size):
    if(size%2==0):
        return (arr[size//2]+arr[size//2-1])/2
    else:
        return arr[size//2]

#helper function getIndex()
# def getIndex(item, arr):
#     ind = 0
#     while(ind<len(arr) and item>arr[ind]):
#         ind+=1
#     return ind

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    #get the list of days to examine!
    days_examined = expenditure[0:d]
    days_examined.sort()
    curr_day = d
    notices = 0
    while(curr_day<len(expenditure)):
        mid = median(days_examined, d)
        if(mid*2<=expenditure[curr_day]):
            notices+=1
            print(mid, curr_day, days_examined)
        days_examined.remove(expenditure[curr_day-d])
        ind = binary_search_recursive(days_examined, expenditure[curr_day], 0, d-2)
        days_examined.insert(ind, expenditure[curr_day])
        curr_day+=1

    return notices


arr = [10, 20, 30, 40, 50]
arr2 = [1, 2, 3, 4, 4]
activityNotifications(arr, 3)
# activityNotifications(arr2, 4)
