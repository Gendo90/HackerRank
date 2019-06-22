#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np

# Complete the freqQuery function below.
def freqQuery(queries):
    val_present = {}
    freq_present = {}
    total_count = []
    total_cycles = 0
    for query in queries:
        total_cycles+=1
        # print(freq_present)
        if(query[0]==1):
            #case where element is the first item added with that value
            if(query[1] not in val_present):
                val_present[query[1]] = 1
                if(freq_present.get(1)):
                    freq_present[1][query[1]] = True
                else:
                    freq_present[1] = {query[1]:True}
            #case where there are already query[1] value(s) present
            else:
                freq_present[val_present[query[1]]].pop(query[1])
                val_present[query[1]] += 1
                if(val_present[query[1]] in freq_present):
                    freq_present[val_present[query[1]]][query[1]] = True
                else:
                    freq_present[val_present[query[1]]] = {query[1]:True}
        elif(query[0]==2):
            #case where the value must be deleted because it is present
            if(query[1] in val_present):
                if(val_present[query[1]]==1):
                    val_present.pop(query[1])
                    freq_present[1].pop(query[1])
                else:
                    freq_present[val_present[query[1]]].pop(query[1])
                    val_present[query[1]]-=1
                    if(val_present[query[1]] in freq_present):
                        freq_present[val_present[query[1]]][query[1]] = True
                    else:
                        freq_present[val_present[query[1]]] = {query[1]:True}
        else:
            if(freq_present.get(query[1])):
                total_count.append(1)
            else:
                total_count.append(0)

    # print(freq_present.keys())
    return total_count, total_cycles



print(freqQuery([(1, 5), (1, 6), (3, 2), (1, 10), (1, 10), (1, 6), (2, 6), (2, 6), (2, 6), (3, 6)]))
# print(freqQuery([(3, 6)]))

if __name__ == '__main__':
    # f = open("freqQueryTest10.txt", 'r')
    #
    # if f.mode == 'r':
    #     contents = f.read()
    #
    # f.close()
    arr = np.genfromtxt(r'freqQueryTest10.txt', delimiter=' ')
    # nr = input().rstrip().split()
    #
    # n = int(nr[0])
    #
    # r = int(nr[1])
    arr_ans = np.genfromtxt(r'freqQuerySoln10.txt', delimiter=' ')

    # arr = list(map(int, contents.rstrip().split()))
    # print(arr)

    ans, a = freqQuery(arr)

    # print(ans)
    print(len(ans))
    print(len(arr_ans))
    print(a)
    print(all(arr_ans==ans))
