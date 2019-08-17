#!/bin/python3

import os
import sys

#helper function to calculate primes
def prime_calc(q):
    #first get a list of the primes to use for the q iterations
    primes = [2]
    checkers = q-1
    val = primes[-1]+1
    test_num = 2
    while(checkers!=0):
        while(val//2>=test_num):
            if(val%test_num==0):
                val+=1
                test_num=2
                continue
            else:
                test_num+=1
        primes.append(val)
        test_num=2
        val+=1
        checkers-=1
    return primes
#
# Complete the waiter function below.
#
def waiter(arr, q):
    primes = prime_calc(q)

    a_orig = arr
    b = {}
    a_new = []
    # print(primes)
    for i, divisor in enumerate(primes):
        while(a_orig):
            this_plate = a_orig.pop()
            if(this_plate%divisor==0):
                if(not b.get(i)):
                    b[i] = [this_plate]
                else:
                    b[i].append(this_plate)
            else:
                a_new.append(this_plate)
        a_orig = a_new
        a_new = []

    output = []
    for i in range(q):
        if(b.get(i)!=None):
            # print(b.get(i), i)
            while(b[i]):
                output.append(b[i].pop())

    if(a_orig):
        while(a_orig):
            output.append(a_orig.pop())

    return output


print(waiter([3, 4, 7, 6, 5], 1))
