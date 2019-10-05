#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np
import collections


#helper function RSelect
def RSelect(arr, size, i):
    if(size==1):
        return arr[1]

    p_ind = random.randint(0, size-1)
    j = partition(arr, size, p_ind)
    # print(p_ind, size)
    #left side of array contains median
    if(j>i):
        return RSelect(arr[:j], j, i)
    #right side of array contains median
    elif(j<i):
        return RSelect(arr[j:], size-j, i-j)
    elif(j==i):
        return arr[p_ind]

#helper function partition
def partition(arr, size, p_ind):
    pivot = arr[p_ind]
    arr[0], arr[p_ind] = arr[p_ind], arr[0]
    lIndex = 0
    rIndex = size-1
    while(True):
        while(lIndex<=rIndex and arr[lIndex] <= pivot):
            lIndex+=1
        while(rIndex>=lIndex and arr[rIndex]>=pivot):
            rIndex-=1
        if(rIndex<=lIndex):
            break
        arr[lIndex], arr[rIndex] = arr[rIndex], arr[lIndex]
    arr[0], arr[rIndex] = arr[rIndex], arr[0]

    return rIndex

def calcMid(scoping, d):
    if(d%2!=0):
        mid = RSelect(scoping, d, d//2)
    else:
        mid = (RSelect(scoping, d, d//2) + RSelect(scoping, d, d//2-1))/2
    return mid

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    #get the list of days to examine!
    days_examined = (expenditure[0:d])
    curr_day = d
    notices = 0
    mid = calcMid(days_examined, d)
    newMid=False
    while(curr_day<len(expenditure)):
        if(newMid==True):
            mid = calcMid(days_examined, d)
        if(mid*2<=expenditure[curr_day]):
            notices+=1
        a=days_examined.pop(0)
        days_examined.append(expenditure[curr_day])
        if((a<mid and expenditure[curr_day]>mid) or (a>mid and expenditure[curr_day]<mid)):
            newMid=False
        else:
            newMid=True
        curr_day+=1
        print(curr_day, end="\n", flush=True)

    return notices


arr = [10, 20, 30, 40, 50]
arr2 = [1, 2, 3, 4, 4]
activityNotifications(arr, 3)
# activityNotifications(arr2, 4)



if __name__ == '__main__':
    sys.setrecursionlimit(2000)
    arr = np.genfromtxt(r'activity_notification.txt', delimiter=' ')
    # nr = input().rstrip().split()
    #
    # n = int(nr[0])
    #
    # r = int(nr[1])
    # arr_ans = np.genfromtxt(r'freqQuerySoln10.txt', delimiter=' ')

    n = 200000

    d = 40001

    expenditure = arr
    print(n)

    result = activityNotifications(list(expenditure), d)

    print(result)
