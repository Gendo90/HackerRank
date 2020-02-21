#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(grid):
    #small grid cases, no cavities possible
    if(len(grid)<3):
        return grid

    grid = [[a for a in line] for line in grid]

    for i in range(1, len(grid)-1):
        for j in range(1, len(grid)-1):
            if(not checkSide(grid, (i, j), -1, 0)):
                continue
            if(not checkSide(grid, (i, j), 1, 0)):
                continue
            if(not checkSide(grid, (i, j), 0, 1)):
                continue
            if(not checkSide(grid, (i, j), 0, -1)):
                continue
            grid[i][j] = "X"

    print(grid)

    return ["".join(line) for line in grid]

def checkSide(arr, a, i_shift, j_shift):
    i = a[0]
    j = a[1]
    if(arr[i+i_shift][j+j_shift]!='X'):
        if(int(arr[i][j])>int(arr[i+i_shift][j+j_shift])):
            return True
    return False



# print(dayOfProgrammer(2016))
# print(dayOfProgrammer(2017))
