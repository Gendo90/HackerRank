import heapq
import sys

if __name__ == "__main__":
    n = int(input())
    heap = []
    #how to get the deletions and heapify to work in O(log(n)) time or less?
    for i in range(n):
        results = list(map(int, input().split(" ")))
        if(len(results)==1):
            print(heap[0])
        else:
            if(results[0]==1):
                heapq.heappush(heap, results[1])
            else:
                curr_val = heap[0]
                k=0
                while(curr_val<results[1]):
                    k+=1
                    curr_val = heap[2*k+1]
                heap.remove(results[1])
                heapq.heapify(heap)

#working code for HackerRank code box
# import sys
# import heapq
#
# if __name__ == "__main__":
#     n = int(input())
#     heap = []
#     #how to get the deletions and heapify to work in O(log(n)) time or less?
#     for i in range(n):
#         this_inp = sys.stdin.readline()
#         results = list(map(int, this_inp.split(" ")))
#         if(len(results)==1):
#             print(heap[0])
#         else:
#             if(results[0]==1):
#                 heapq.heappush(heap, results[1])
#             else:
#                 heap.remove(results[1])
#                 heapq.heapify(heap)
