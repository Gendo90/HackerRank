import heapq
import os
import sys

#
# Complete the runningMedian function below.
#
def runningMedian(arr):
    lower_heap = []
    upper_heap = [arr[0]]
    lower_heap_len = 0
    upper_heap_len = 1
    print("{:.1f}".format(arr[0]*1.0))

    for i, item in enumerate(arr[1:][:]):
        # print(i, item, lower_heap, upper_heap)
        if(item<upper_heap[0]):
            heapq.heappush(lower_heap, -item)
            lower_heap_len+=1
        else:
            heapq.heappush(upper_heap, item)
            upper_heap_len+=1
        if(i%2==0):
            if(upper_heap_len>lower_heap_len):
                removed = heapq.heappop(upper_heap)
                heapq.heappush(lower_heap, -removed)
                upper_heap_len-=1
                lower_heap_len+=1
            elif(upper_heap_len<lower_heap_len):
                removed = heapq.heappop(lower_heap)
                heapq.heappush(upper_heap, -removed)
                upper_heap_len+=1
                lower_heap_len-=1
            avg = (upper_heap[0]-lower_heap[0])/2
            print("{:.1f}".format(avg*1.0))
        else:
            if(upper_heap_len>lower_heap_len):
                med = upper_heap[0]
            else:
                med = -lower_heap[0]
            print("{:.1f}".format(med*1.0))

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

runningMedian(arr)
