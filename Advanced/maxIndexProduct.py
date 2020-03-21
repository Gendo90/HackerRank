#!/bin/python3

import os
import sys
import numpy as np

# Complete the solve function below.
def solve(arr):
    n = len(arr)
    latest = max(arr)
    maxInd = arr.index(latest)
    prods = []
    lastSeen = {"beforeLargest":[arr[0], 0], "afterLargest":[int(latest), maxInd, arr.count(latest)-1] }

    for i in range(n):
        if(i==0 or i==n-1):
            prods.append(0)
            continue

        currVal = arr[i]
        #case where the left will be 0 -> no need to check all previous elements!
        if(currVal>lastSeen["beforeLargest"][0]):
            lastSeen["beforeLargest"] = [currVal, i]
            #might also be new largest value! What a trick!
            if(arr[i]==lastSeen["afterLargest"][0]):
                if(lastSeen["afterLargest"][2] == 0):
                    nextLargest = max(arr[i+1:])
                    lastSeen["afterLargest"] = [int(nextLargest), arr[i+1:].index(nextLargest), arr[i+1:].count(nextLargest)-1]
                else:
                    #still more of that max number remaining to the right!
                    lastSeen["afterLargest"][2] -= 1
            prods.append(0)
            continue
        elif(currVal==lastSeen["beforeLargest"][0]):
            prods.append(0)
            continue

        # case where the right will be 0 -> no need to check all previous elements!
        #make sure the count of max numbers remaining is zero!
        if(arr[i]==lastSeen["afterLargest"][0]):
            if(lastSeen["afterLargest"][2] == 0):
                nextLargest = max(arr[i+1:])
                lastSeen["afterLargest"] = [int(nextLargest), arr[i+1:].index(nextLargest), arr[i+1:].count(nextLargest)-1]
            else:
                #still more of that max number remaining to the right!
                lastSeen["afterLargest"][2] -= 1
            prods.append(0)
            continue

        j = i-1
        while(j>=0 and arr[j]<=currVal):
            j-=1
        if(j==-1):
            prods.append(0)
            continue
        left = j+1

        k = i+1
        while(k<n and arr[k]<=currVal):
            k+=1
        if(k==n):
            prods.append(0)
            continue
        right = k+1
        # print(left, right, i)
        prods.append(left*right)

    return max(prods)

print(solve([5, 4, 3, 4, 5]))
print(solve([6, 1, 9, 3, 2]))

if __name__ == '__main__':
    # f = open("freqQueryTest10.txt", 'r')
    #
    # if f.mode == 'r':
    #     contents = f.read()
    #
    # f.close()
    arr = np.genfromtxt(r'input12.txt', delimiter=' ')

    print(solve(list(arr)))
