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

def calcMid(h_lower, h_upper, avg):
    if(avg):
        mid = (h_lower[-1]+h_upper[0])/2
    else:
        mid = h_upper[0]
    return mid

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
    lower_dict = {}
    upper_dict = {}
    h_lower = sorted_days[0:d//2-1]
    heapq.heapify(h_lower)
    for i, item in enumerate(h_lower):
        lower_dict[item] = i

    h_upper = sorted_days[d//2:]
    heapq.heapify(h_upper)
    # print(h_upper)
    for i, item in enumerate(h_upper):
        upper_dict[item] = i
    if(d%2==0):
        avg = True
    else:
        avg = False
    mid = calcMid(h_lower, h_upper, avg)
    newMid=False
    while(curr_day<len(expenditure)):
        print(mid)
        if(newMid==True):
            mid = calcMid(h_lower, h_upper, avg)
        if(mid*2<=expenditure[curr_day]):
            notices+=1
        a=expenditure[curr_day-d]
        days_examined.append(expenditure[curr_day])
        if((a<mid and expenditure[curr_day]>mid) or (a>mid and expenditure[curr_day]<mid)):
            newMid=False
        else:
            if(a<mid and expenditure[curr_day]<mid):
                heapq.heappush(h_lower, expenditure[curr_day])
                #remove last day element
                ind = lower_dict.get(a)
                removeEarliestDay(h_lower, ind)
                for item in lower_dict.keys():
                    if(item>=ind):
                        lower_dict[item]-=1
                else:
                    lower_dict[h_lower[ind]] = ind
            elif(a>=mid and expenditure[curr_day]>=mid):
                heapq.heappush(h_upper, expenditure[curr_day])
                #remove last day element
                ind = upper_dict.get(a)
                removeEarliestDay(h_upper, ind)
                for i, item in enumerate(h_upper[ind:]):
                    upper_dict[item] = i
            newMid=True
        curr_day+=1
        print(curr_day, end="\n", flush=True)

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
