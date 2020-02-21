import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    #put into buckets based on remainder
    remainders = {}
    maxSubset = 0
    for i in range(k):
        remainders[i] = 0

    for item in s:
        remainders[item%k]+=1

    # print(remainders)

    #special case for k=1
    #their solution did not have that there needed to be two values or more
    #in the input array for the k=1 case to be valid (e.g. valid with s=[1])
    #but I left it in here because it seems more right...
    if(k==1 and len(s)>1):
        return 1

    #can only have up to one evenly divisible number - other will make it
    #a divisible subset, but only add if there are numbers with remainders
    if(remainders[0]!=len(s) and remainders[0]>0):
        maxSubset=1
    remainders.pop(0)

    #add up to one middle value if k is even, if there is a middle value
    #remainder
    if(k%2==0 and remainders[k/2]>0):
        maxSubset+=1
        remainders.pop(k/2)
    # print(maxSubset)
    #combine remainders to see which max subset values are possible
    #choose greater of each "complementary" remainder
    for i in range(0, k//2):
        first = i+1
        complement = k-first
        if(first==(k/2)):
            break
        maxSubset += max(remainders[first], remainders[complement])

    return maxSubset


print(nonDivisibleSubset(4, [19,10,12,10,24,25,22]))
print(nonDivisibleSubset(3, [1, 7, 2, 4]))
print(nonDivisibleSubset(1, [1,2,3,4,5]))
