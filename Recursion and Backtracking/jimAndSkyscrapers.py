#!/bin/python3

import os
import sys
from collections import defaultdict

def sumTo(x):
    total = 0
    for i in range(x):
        total+=i

    return total

# Complete the solve function below.
def solve(arr):
    arr_size = len(arr)
    if(arr_size==0):
        return 0

    #add a shortcut for the special "valley" case
    valley_case = False
    valley_map = defaultdict(int)
    currMin = min(arr)
    seenMin = False
    last = float("inf")
    for item in arr:
        if(seenMin):
            if(last>item):
                break
        else:
            if(last<item):
                break
            if(item==currMin):
                seenMin = True
        valley_map[item]+=1
        last = item

    else:
        valley_case = True

    #poor case for general solution, but can be short-circuited here
    if(valley_case):
        print("IS VALLEY CASE")
        total = 0
        for item in valley_map.values():
            total+=sumTo(item)*2
        print(sum(valley_map.values()))

        return total

    currMax = max(arr)
    num_max = 0
    max_locations = [0]
    arr_ranges = []
    for i, val in enumerate(arr):
        if(val==currMax):
            num_max+=1
            max_locations.append(i)
            if(num_max!=1):
                arr_ranges.append((max_locations[num_max-1]+1, i))
            else:
                arr_ranges.append((max_locations[num_max-1], i))

    # if(num_max>1):
    arr_ranges.append((max_locations[-1]+1, arr_size))
    # else:
    #     arr_ranges.append((max_locations[-1]+1, arr_size))
    #     arr_ranges.append((0, max_locations[-1]))

    #now add all lower sums recursively! for each inclusive range between
    #maximum heights
    if(num_max < 2):
        total = 0
    else:
        total = sumTo(num_max)*2

    for min_ind, max_ind in arr_ranges:
        # print(min_ind, max_ind)
        total+= solve(arr[min_ind:max_ind])
        # print(total)

    return total


# print(solve([3, 2, 1, 2, 3, 3]))
# print(solve([1 for i in range(5000)]))

if __name__ == '__main__':

    fileHandler = open("input07_jim.txt", "r")

    # Get list of all lines in file
    listOfLines = fileHandler.readlines()

    # Close file
    fileHandler.close()

    n = int(listOfLines[0])
    arr = list(map(int, listOfLines[1].split(" ")))

    print(solve(arr))
