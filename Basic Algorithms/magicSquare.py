#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    #first, make a map of duplicate numbers
    seen = {}
    for i in range(1, 10):
        seen[i] = 0

    #populate the map of numbers seen
    for i in range(3):
        for j in range(3):
            seen[s[i][j]]+=1

    #find which numbers are missing, put in an ordered list
    #put the duplicates in an ordered list as well
    missing = []
    duplicates = []
    for i in range(1, 10):
        if(seen[i]==0):
            missing.append(i)
        elif(seen[i]>1):
            duplicates += [i for j in range(seen[i]-1)]

    #figure out

    print(missing, duplicates)

    #copy the s grid to compare with later for scoring
    s_copy = [[s[j][i] for i in range(3)] for j in range(3)]

    #set of elements that were changed out, can find the minimum cost
    #by comparing to original grid (see what each change was & calculate the
    #difference)
    while(missing):
        lowest_missing = missing.pop(0)
        lowest_duplicate = duplicates.pop(0)

        replaced = False

        for i in range(len(s_copy)):
            for j in range(len(s_copy[0])):
                if(s_copy[i][j]==lowest_duplicate):
                    arr = getRowScores((i, j), s_copy)
                    if(15 not in arr):
                        s_copy[i][j] = lowest_missing
                        replaced = True
                        break
            if(replaced):
                break

    #now repeat until all rows add to 15
    while(len(getInvalidRows(s_copy))!=8):
    # for k in range(5):
        #populate the exchangeable values
        locations = {}
        values = []

        print(s_copy, "Hello")

        for i in range(len(s_copy)):
            for j in range(len(s_copy[0])):
                arr = getRowScores((i, j), s_copy)
                print(arr, s_copy[i][j], (i, j))
                if(15 not in arr):
                    values.append(s_copy[i][j])
                    locations[values[-1]] = (i, j)

        # print(s_copy)

        #swap minimum diff in values (could get into a inf while loop?) WRONG
        #instead, swap to make a row/col/diagonal work, min difference
        values.sort()
        print(values)
        if(len(values)==0):
            break
        max_diff = 10
        switch_val1, switch_val2 = 0, 0
        for i, val in enumerate(values):
            for j in range(i+1, len(values)):
                if(abs(val-values[j])<max_diff):
                    switch_val1 = val
                    switch_val2 = values[j]
                    max_diff = abs(val-values[j])


        #now switch the values
        val1_loc = locations[switch_val1]
        val2_loc = locations[switch_val2]
        s_copy[(val1_loc[0])][(val1_loc[1])] = switch_val2
        s_copy[(val2_loc[0])][(val2_loc[1])] = switch_val1


    #remove rows that are already valid - no need to change them any more

    #find numbers that need to be changed, then test change each one to fit a
    #single row, and see how many rows are fixed/better - most rows changed
    #is the number that must change
    score = 0
    for i in range(len(s)):
        for j in range(len(s[0])):
            if(s[i][j]!=s_copy[i][j]):
                score+=abs(s[i][j]-s_copy[i][j])

    print(s, s_copy)

    return score

#figure out the sum of the row and col (and sometimes diag) of an element
def getRowScores(a, grid):
    i = a[0]
    j = a[1]
    output_scores = []
    nums = set()

    #get row score, only if no duplicate numbers present
    for k in range(3):
        nums.add(grid[i][k])


    if(len(nums)==3):
        output_scores.append(sum(l for l in grid[i]))

    nums.clear()


    #get col score
    for k in range(3):
        nums.add(grid[k][j])

    if(len(nums)==3):
        output_scores.append(sum(grid[k][j] for k in range(3)))

    nums.clear()


    #get diag score if necessary
    nums2 = set()
    for k in range(3):
        nums.add(grid[k][k])
        nums2.add(grid[k][2-k])

    for i in range(3):
        #main diagonal
        if(a==(i, i) and len(nums)==3):
            output_scores.append(sum(grid[l][l] for l in range(3)))
        #other diagonal
        if(a==(i, 2-i) and len(nums2)==3):
            output_scores.append(sum(grid[l][2-l] for l in range(3)))

    nums.clear()
    nums2.clear()

    return output_scores


def getInvalidRows(grid, magic_num=15):
    validRows = {}
    problem_rows = {}
    #rows designated 1 thru 8
    for i in range(1, 9):
        problem_rows[i]=0

    for i in range(3):
        #get row problems
        if(sum(grid[i])!=magic_num):
            problem_rows[i+1] = sum(grid[i])

        #get col problems
        if(sum(a[i] for a in grid)!=magic_num):
            problem_rows[i+4] = sum(a[0] for a in grid)

    #get diag problems
    if(sum(grid[i][i] for i in range(3))!=magic_num):
        problem_rows[7] = sum(grid[i][i] for i in range(3))

    #get diag problems II
    if(sum(grid[i][2-i] for i in range(3))!=magic_num):
        problem_rows[8] = sum(grid[i][2-i] for i in range(3))

    for i in range(1, 9):
        if(problem_rows[i]==0):
            problem_rows.pop(i)
            validRows[i] = True

    return validRows


grid = [[4, 8, 2],[4, 5, 7],[6, 1, 6]]

print(formingMagicSquare(grid), "final")
# print(formingMagicSquare([[5, 5, 5],[5, 5, 5],[5, 5, 5]]), "final")
print(formingMagicSquare([[5, 3, 4],[1, 5, 8],[6, 4, 2]]), "final")
print(formingMagicSquare([[4,9,2],[3,5,7],[8,1,5]]), "final")
print(formingMagicSquare([[4,5,8],[2,4,1],[1,9,7]]), "final")
# print(getInvalidRows(grid))
