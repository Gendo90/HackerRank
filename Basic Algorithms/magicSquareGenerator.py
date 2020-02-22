#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
#note: read the links in the future! would have saved a bunch of time
def formingMagicSquare(s):
    #basic square
    square = [[8, 3, 4], [1, 5, 9], [6, 7, 2]]

    #rotated original square
    grids = [[[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[6, 1, 8], [7,5,3], [2, 9, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
        [[4, 9, 2], [3, 5, 7], [8,1,6]]
    ]

    #check that rotate works!
    for i in range(4):
        if(rotate(square, i)!=grids[i]):
            print(rotate(square, i), grids[i])

    #reflect all squares!
    grids+=[reflect(item) for item in grids]
    # print(grids)

    scores = []

    for grid in grids:
        scores.append(getScore(grid, s))

    return min(scores)

def reflect(square):
    square2 = []
    for i in range(len(square)):
        row = []
        for j in range(len(square[0])):
            row.append(square[i][len(square)-j-1])
        square2.append(row)
    return square2

#t is number of 90 degree rotations clockwise (can be negative)
def rotate(square, t):
    if(t%4==0):
        return square
    elif(t%4==1):
        return rotateOnce(square)
    elif(t%4==2):
        square2 = rotateOnce(square)
        return rotateOnce(square2)
    else:
        square2 = rotateOnce(square)
        square3 = rotateOnce(square2)
        square4 = rotateOnce(square3)
        return square4


def rotateOnce(square):
    rotatedSquare = [[] for i in range(len(square))]
    for i in range(len(square)):
        for j in range(len(square[0])):
            rotatedSquare[j].insert(0, square[i][j])

    return rotatedSquare


def getScore(grid1, grid2):
    score = 0
    for i in range(len(grid1)):
        for j in range(len(grid1[0])):
            score += abs(grid1[i][j]-grid2[i][j])

    return score

#only works for a+b right now, not a+b+c
def calcSumCombinations(numbers):
    sums = {}
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            a = numbers[i]
            b = numbers[j]
            thisSet = set()
            thisSet.add(a)
            thisSet.add(b)
            if(a+b not in sums):
                sums[a+b] = [thisSet]
            else:
                sums[a+b].append(set(thisSet))
    return sums

#let n be the number of items to be summed e.g. 2 is couplets, 3 is triplets,
#etc. for an nxn magic square, where n>=3
def sum_Xlets(n):
    target_sum = sum(range(1, n**2+1))/n
    # print(target_sum)
    #use symmetry to find xlets!
    nums = {}
    vals = []
    for i in range(1, n**2//2+1):
        #middle set is unnecessary - will always be in the middle!
        if(n%2!=0 and i==(n**2//2+1)):
            continue
        nums[i] = set()
        nums[i].add(i)
        nums[i].add(n**2+1-i)
        vals.append(i)
        if(n%2!=0):
            #add middle value for odd number sides
            nums[i].add(n**2//2+1)
    print(nums)
    #now can combine any of the couplets given here with any other couplet
    #until the size of the xLet is n
    base_units = [(nums[key]) for key in nums.keys()]

    # print(base_units)

    #combine them (at random, in this situation) until all xlets have formed
    while(min([len(a) for a in base_units])<n):
        a = random.randint(0, len(base_units)-1)
        b = random.randint(0, len(base_units)-1)
        if(a!=b and (len(base_units[a])==len(base_units[b])) and
            (len(base_units[a])==min([len(c) for c in base_units]))):
            base_units[a] = base_units[a].union(base_units[b])
            base_units.pop(b)

    return base_units

    #set of sets has what you want!


def generateMagicSquare(n):
    values = [a for a in range(1, n**2+1)]
    magicSquare = [[0 for i in range(n)] for j in range(n)]
    side_total = sum(range(1, n**2+1))/n
    print(side_total)
    print(sum_Xlets(4))
    numbers = [a for a in values if(a!=7 and a!=8 and a!=9 and a!=10)]
    output_map = calcSumCombinations(numbers)
    print(list(output_map[l] for l in range(15, 20)))
    if(n%2!=0):
        middle = n//2
        magicSquare[n//2][n//2] = middle

    # print

    return magicSquare

print(generateMagicSquare(4))



#some combination of these values reaches a target number
def getToNumber(desiredNum, values, n):
    num_map = {}
    for value in values:
        num_map[value] = {}
        test = set(values)
        test.pop(value)
        #assuming the value is not the desiredNum
        # for i in range(1, n)
        #     for item in test:
        #         if(desiredNum-item==0):
        #             num_map[value][item] = True
        #         elif(desiredNum-item>0):
        #             num_map[value][item] = desiredNum-item
        #
    return num_map

#exponential function? - use caution!
#upgrade with memoization at some point!
#maybe include a filter, to limit the depth of the recursion (e.g. only need 3 factors, or 4)
def recursiveSums(desiredNum, values):
    # print(values)
    if(len(values)==1):
        if(values[0]==desiredNum):
            return values[0]
    else:
        arr = []
        removals = []
        for i, value in enumerate(values):
            thisDesiredNum = desiredNum-value
            if(thisDesiredNum==0):
                arr.append(value)
                removals.append(value)
            elif(thisDesiredNum>0):
                newValues = values[:]
                newValues.pop(i)
                arr.append([value])
                # print(thisDesiredNum)
                arr[-1].extend(recursiveSums(thisDesiredNum, newValues))
                if(len(arr[-1])==0 or arr[-1]==[value]):
                    arr.pop()
            removals.append(value)
        #remove unusable values
        # print("arr is ", arr, removals)
        # print("desired num is ", desiredNum)
        iteratedValues = [value for value in values if(value not in removals)]
        if(iteratedValues):
            # print("values left are ", iteratedValues)
            arr.append(recursiveSums(desiredNum, iteratedValues))
        return arr


def convertSumsToMap(arr, values):
    num_map = {}
    for item in values:
        num_map[item] = []

    for i in range(len(arr)):
        num_map[i+1] = setFromValues(arr[i])

    return num_map

#recursively gather up the nested arrays into sets
def setFromValues(arr):
    if(isinstance(arr, int)):
        return arr
    num = arr.pop(0)
    # print(num)
    currSet = set()
    currSet.add(num)
    allSets = [currSet]
    for i in range(len(arr)):
        if(isinstance(arr[i], int)):
            currSet.add(arr[i])
        else:
            newSet = set()
            newSet.add(num)
            nestedSets = setFromValues(arr[i])
            # print(nestedSets)
            for a in nestedSets:
                newSet = newSet.union(a)
                if(newSet not in allSets):
                    allSets.append(newSet)
                newSet = set()
                newSet.add(num)
    # print(allSets, currSet, num)
    #case where there are no matches for the first item
    if(len(allSets[0])==1):
        allSets.pop(0)
    return allSets

a = [i for i in range(1, 36)]
# print(calcSumCombinations(a)[10])

n = recursiveSums(36, a)
# print(n[1], "Hello")

print(convertSumsToMap(n, a))

k = 6
target_sum = sum(range(1, k**2+1))/k
print(target_sum)

# #figure out the sum of the row and col (and sometimes diag) of an element
# def getRowScores(a, grid):
#     i = a[0]
#     j = a[1]
#     output_scores = []
#     nums = set()
#
#     #get row score, only if no duplicate numbers present
#     for k in range(3):
#         nums.add(grid[i][k])
#
#
#     if(len(nums)==3):
#         output_scores.append(sum(l for l in grid[i]))
#
#     nums.clear()
#
#
#     #get col score
#     for k in range(3):
#         nums.add(grid[k][j])
#
#     if(len(nums)==3):
#         output_scores.append(sum(grid[k][j] for k in range(3)))
#
#     nums.clear()
#
#
#     #get diag score if necessary
#     nums2 = set()
#     for k in range(3):
#         nums.add(grid[k][k])
#         nums2.add(grid[k][2-k])
#
#     for i in range(3):
#         #main diagonal
#         if(a==(i, i) and len(nums)==3):
#             output_scores.append(sum(grid[l][l] for l in range(3)))
#         #other diagonal
#         if(a==(i, 2-i) and len(nums2)==3):
#             output_scores.append(sum(grid[l][2-l] for l in range(3)))
#
#     nums.clear()
#     nums2.clear()
#
#     return output_scores
#
#
# def getInvalidRows(grid, magic_num=15):
#     validRows = {}
#     problem_rows = {}
#     #rows designated 1 thru 8
#     for i in range(1, 9):
#         problem_rows[i]=0
#
#     for i in range(3):
#         #get row problems
#         if(sum(grid[i])!=magic_num):
#             problem_rows[i+1] = sum(grid[i])
#
#         #get col problems
#         if(sum(a[i] for a in grid)!=magic_num):
#             problem_rows[i+4] = sum(a[0] for a in grid)
#
#     #get diag problems
#     if(sum(grid[i][i] for i in range(3))!=magic_num):
#         problem_rows[7] = sum(grid[i][i] for i in range(3))
#
#     #get diag problems II
#     if(sum(grid[i][2-i] for i in range(3))!=magic_num):
#         problem_rows[8] = sum(grid[i][2-i] for i in range(3))
#
#     for i in range(1, 9):
#         if(problem_rows[i]==0):
#             problem_rows.pop(i)
#             validRows[i] = True
#
#     return validRows


grid = [[4, 8, 2],[4, 5, 7],[6, 1, 6]]

print(formingMagicSquare(grid), "final")
# print(formingMagicSquare([[5, 5, 5],[5, 5, 5],[5, 5, 5]]), "final")
print(formingMagicSquare([[5, 3, 4],[1, 5, 8],[6, 4, 2]]), "final")
print(formingMagicSquare([[4,9,2],[3,5,7],[8,1,5]]), "final")
print(formingMagicSquare([[4,5,8],[2,4,1],[1,9,7]]), "final")
print(formingMagicSquare([[2, 9, 8],[4, 2, 7],[5, 6, 7]]), "final")
print(formingMagicSquare([[4, 4, 7],[3,1,5],[1,7,9]]), "final")
# print(getInvalidRows(grid))
