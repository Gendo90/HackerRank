#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the riddle function below.
#partial solution, too slow!
def riddle(arr):
    # complete this function
    output = [max(arr)]
    smallest = min(arr)
    n = len(arr)
    for i in range(2, n):
        test = arr[0:i]
        check = []
        for j in range(i, n):
            # print(test)
            check.append(min(test))
            test.pop(0)
            test.append(arr[j])
        else:
            check.append(min(test))

        output.append(max(check))

        if(output[-1]==smallest):
            k = i
            while(k<n-1):
                output.append(min(arr))
                k+=1
            break


    output.append(min(arr))

    return output


print(riddle([3, 5, 4, 7, 6, 2]))

#upgraded solution
def riddle2(arr):
    #last item in array first!
    smallest = min(arr)
    largest = max(arr)
    output = [largest]
    locations = {smallest:[]}
    lower = []
    upper = []
    n = len(arr)
    #like the bacteria growth problem
    for i, item in enumerate(arr):
        if(item==smallest):
            locations[smallest].append(i)

    #only get the largest if largest is subsumed by smallest
    #wrong, need to account for max changing when near smaller numbers
    for i in range(len(arr)-1):
        calcNewMax = False
        if(i==0):
            #add uppers and lowers
            for location in locations[smallest]:
                if(location-1>=0):
                    lower.append(location-1)
                if(location+1<n):
                    upper.append(location+1)

        lower_removals = []
        for j in range(len(lower)):
            if(arr[lower[j]]==smallest):
                lower_removals.append(lower[j])
                continue
            if(arr[lower[j]]==largest):
                calcNewMax = True
            arr[lower[j]] = smallest
            if(lower[j]>=0):
                lower[j]-=1
            else:
                lower_removals.append(lower[j])

        upper_removals = []
        # print(upper)
        for j in range(len(upper)):
            if(arr[upper[j]]==smallest):
                upper_removals.append(upper[j])
                continue
            if(arr[upper[j]]==largest):
                calcNewMax = True
            arr[upper[j]] = smallest
            if(upper[j]<n-1):
                upper[j]+=1
            else:
                upper_removals.append(upper[j])

        for removal in lower_removals:
            lower.remove(removal)

        for removal in upper_removals:
            upper.remove(removal)

        if(calcNewMax):
            largest = max(arr)
            output.append(largest)
        else:
            output.append(largest)

    return output

print(riddle2([1, 2, 3, 5, 1, 13, 3]))
print(riddle2([3, 5, 4, 7, 6, 2]))


#correct, but still not fast enough!
def riddle3(arr):
    #compare each resulting number to its neighbors and return the minimum of the
    #results
    n = len(arr)
    test = arr[:]
    output = [max(arr)]
    for i in range(n-1):
        test, this_max = reductionStep(test)
        output.append(this_max)

    return output

def reductionStep(arr):
    n = len(arr)
    output = []
    max_val = -1
    for i in range(n-1):
        new_val = min(arr[i], arr[i+1])
        if(new_val>max_val):
            max_val = new_val
        output.append(new_val)

    return output, max_val

print(riddle3([1, 2, 3, 5, 1, 13, 3]))
print(riddle3([3, 5, 4, 7, 6, 2]))
