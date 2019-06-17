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

#helper function to count up thirds and seconds and multiply them
#not as efficient as just using a formula but more accurate
#call this function if modified so that it looks in a hash map and
#counts the items if they are in it, and adds them - more generalized than
# just for these two "second" and "third" items?
def countUp(arr, i, second, third):
    total = 0
    #put code here to only count this value above current index
    check_arr = [a for a in arr[i+1:] if(a==second or a==third)]
    second_left = check_arr.count(second)
    third_left = check_arr[1:].count(third)
    for item in (check_arr):
        if(item==second):
            total+=third_left
            second_left-=1
        elif(item==third):
            third_left-=1
        if(second_left==0 or third_left==0):
            break

    return total

# output redirection for review
def redirect_to_file(text):
    original = sys.stdout
    sys.stdout = open('redirect.txt', 'w')
    print('This is your redirected text:')
    print(text)
    sys.stdout = original

# Complete the countTriplets function below.
def countTriplets(arr, r):
    tripletCount = 0
    # need to examine original arr to know how many indexes are above
    # a certain value for the i<j<k requirement to hold
    arr = list(arr)
    arr2 = sorted(arr)
    starting_progs = {}
    first_seen = {}
    seconds = {}
    thirds = {}
    remember = ""
    #keep hashmap of values to the right, subtract if seen!
    #keep hashmap of values still to be multiplied, number to be multiplied

    # populate the "look for" hash map, to know which values to count
    # only stores valid triplets that can be found
    for i, item in enumerate(arr2):
        second = item*r
        third = second*r

        if item not in starting_progs:
            if (binary_search_recursive(arr2, second, i, len(arr2)-1)!=-1):
                if (binary_search_recursive(arr2, third, i, len(arr2)-1)!=-1):
                    starting_progs[item] = True
                    seconds[second] = True
                    thirds[third] = 0

    #need to use the original array to check indexes easier
    for i, item in enumerate(arr):
        #first is the first of the possible triplets
        #can also backtrack to get correct answer
        if(item not in first_seen):
            first_seen[item]=1
        else:
            first_seen[item]+=1

        next = item*r
        third = second*r

        # print(thirds)
        if(item in seconds and thirds[next]==0):
            thirds[next] = arr[i+1:].count(next)
        # remember+= str(seen) + " " + str(tripletCount) + "\n"
        #current item is a second value in a progression
        if(item in seconds and r!=1):
            #add values to triplets
            if(not first_seen.get(item/r)):
                first_seen[item/r] = 0
            # print(seen, first_seen, i)
            tripletCount+=thirds[next]*first_seen[item/r]
        elif(r==1):
            tripletCount+=(thirds[next])*(thirds[next]-1)/2
            thirds[next]-=1


        # third item, must reduce count of those items by one
        if(item in thirds and r!=1):
            if(thirds[item]!=0):
                thirds[item]-=1

    # redirect_to_file(remember)
    return int(tripletCount)

print(countTriplets(numpy.ones(100), 1)) #returns 7 should be 5

if __name__ == '__main__':
    f = open("countTripletsTest6.py", 'r')

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
