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


def getScore(grid1, grid2):
    score = 0
    for i in range(len(grid1)):
        for j in range(len(grid1[0])):
            score += abs(grid1[i][j]-grid2[i][j])

    return score

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
