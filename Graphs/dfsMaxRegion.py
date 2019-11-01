#!/bin/python3

import math
import os
import random
import re
import sys

#can probably use a bfs anyway...
def bfs_matrix(start, grid, seen):
    count = 0
    queue = [start]
    this_seen = {}
    while(queue):
        curr = queue.pop(0)
        if(curr in this_seen and this_seen[curr]!=1):
            continue
        else:
            if(grid[curr[0]][curr[1]]==1):
                if(curr not in this_seen):
                    this_seen[curr]=1
                    count+=1
            else:
                this_seen[curr]=0
            if(this_seen[curr]==1):
                for i in range(curr[0]-1, curr[0]+2):
                    for j in range(curr[1]-1, curr[1]+2):
                        if(i<0 or len(grid)==i or j<0 or len(grid[0])==j):
                            continue
                        if((i, j) in this_seen):
                            continue
                        queue.append((i, j))

    return count, this_seen



# Complete the maxRegion function below.
def maxRegion(grid):
    seen = {}
    largest = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if ((i, j) not in seen):
                reg, explored = bfs_matrix((i, j), grid, seen)
                if(reg>largest):
                    largest = reg
                seen.update(explored)

    return largest
