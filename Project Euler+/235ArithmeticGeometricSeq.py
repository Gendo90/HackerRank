#!/bin/python3

import math
import os
import random
import re
import sys
import time
import scipy.optimize
# import numpy
# import sympy

# calculate r for the given sequence to return -x
def calcR(a, d, n, x):

    # correct equation!
    # working with scipy & fsolve
    func = lambda r : x+((a-d*((1-r**n)/(1-r))-(a-n*d)*(r**n))/(1-r))
    r_solution = scipy.optimize.fsolve(func, 1.01)

    #works better (more accurate/more digits) with newton_krylov...
    # Unless the guess is too far off
    # r_solution = scipy.optimize.newton_krylov(func, 1.01, verbose=True)

    # working with sympy? Not really...
    # r = sympy.Symbol("r")
    # f1 = x+((a-d*((1-r**n)/(1-r))-(a-n*d)*(r**n))/(1-r))
    # r_solution = sympy.nsolve((f1), (r), (1.001), verify=False)

    return r_solution


def calcX(a, d, n, r):
    total = 0
    for k in range(1, n+1):
        total+= (a-d*k)*(r**(k-1))

    return total

l = calcR(1, 1, 3000, 10000000000)
print(l)
# print(round(l[0], 13))
print(calcX(1, 1, 3000, l))

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    for i in range(n):

        arr = list(map(int, input().rstrip().split()))

        res = calcR(arr[0], arr[1], arr[2], arr[3])
        res = round(res[0], 12)
        print(res)
        print(calcX(arr[0], arr[1], arr[2], round(res[0], 12)))
