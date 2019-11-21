#!/bin/python3

import os
import sys
import heapq
import numpy as np

#
# Complete the cookies function below.
#
def cookies(k, A):
    heap = A
    heapq.heapify(heap)
    count = 0
    #case where there may be too few elements to run the while loop
    if(not heap):
        return -1
    if(len(heap)<2):
        if(heap[0]<k):
            return -1
        else:
            return count

    while(heap[0]<k and len(heap)>=2):
        smallest_val = heapq.heappop(heap)
        second_smallest = heapq.heappop(heap)
        new_val = smallest_val+2*second_smallest
        heapq.heappush(heap, new_val)
        count+=1
    # print(heap)
    #check if smallest element is less than k or not when the loop condiitons
    #are met
    if(len(heap)<2):
        if(heap[0]<k):
            return -1
        else:
            return count

    return count



# 67800 291140174 for 12
# 100000 578646143 for 14
if __name__ == "__main__":
    k = 578646143

    arr = list(np.genfromtxt("cookies_input14.txt", delimiter=" "))

    print(cookies(k, arr))
