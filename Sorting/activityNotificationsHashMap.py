#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np
import collections
import heapq


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

def calcMid(dict, d, avg):
    curr = 0
    a=d//2
    b=d//2-1
    if(avg):
        curr2=0
        for item in dict.keys():
            if(a<0):
                break
            curr = item
            a-=dict[item]

        for item in dict.keys():
            if(b<0):
                break
            curr2 = item
            b-=dict[item]
        return (curr+curr2)/2

    else:
        for item in dict.keys():
            if(a<0):
                break
            curr = item
            a-=dict[item]

    return curr

def removeEarliestDay(h, i):
    h[i] = h[-1]
    h.pop()
    if i < len(h):
        heapq._siftup(h, i)
        heapq._siftdown(h, 0, i)

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    #get the list of days to examine!
    days_examined = (expenditure[0:d])
    curr_day = d
    notices = 0
    sorted_days = sorted(days_examined)
    dict = {}
    for i in range(0, 201):
        dict[i] = 0
    for item in sorted_days:
        dict[item]+=1
    if(d%2==0):
        avg = True
    else:
        avg = False
    mid = calcMid(dict, d//2, avg)
    while(curr_day<len(expenditure)):
        # print(mid)
        #a is the expenditure added today
        a = expenditure[curr_day]
        #b is the expenditure that is removed next
        b = expenditure[curr_day-d]
        mid = calcMid(dict, d, avg)
        if(mid*2<=a):
            notices+=1

        dict[a]+=1
        dict[b]-=1


        curr_day+=1
        # print(curr_day, end="\n", flush=True)

    return notices


arr = [10, 20, 30, 40, 50]
arr2 = [1, 2, 3, 4, 4]
# activityNotifications(arr, 3)
activityNotifications(arr2, 4)



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

    expenditure = list(map(int, arr))
    # print(n)

    result = activityNotifications(expenditure, d)

    print(result)
