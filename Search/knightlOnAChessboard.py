#!/bin/python3

import math
import os
import random
import re
import sys

# n is 5 to 25

# Complete the knightlOnAChessboard function below.
def knightlOnAChessboard(n):
    # breadth-first search
    # with dynamic programming elements to count moves
    # and find the minimum

    #how the different knights can move
    different_knight_moves = [(b, a) for a in range(1, n) for b in range(1, n)]

    #output array of moves for each knight
    min_moves = []

    # print(different_knight_moves)

    for item in different_knight_moves:
        # implement breadth-first seach terminating when the knight reaches
        # square (n-1, n-1) or has no spots left to search
        saved_spots = {(0, 0):0}
        queue = [(0, 0)]

        #start breadth-first seach!
        while(queue):
            this_square = queue.pop(0)
            # account for eight (8) possible moves!
            if(0<=(this_square[0]+item[0])<n):
                if(0<=(this_square[1]+item[1])<n):
                    current = (this_square[0]+item[0], this_square[1]+item[1])
                    if(current not in saved_spots):
                        queue.append(current)
                        saved_spots[current] = saved_spots[this_square]+1
                if(0<=(this_square[1]-item[1])<n):
                    current = (this_square[0]+item[0], this_square[1]-item[1])
                    if(current not in saved_spots):
                        queue.append(current)
                        saved_spots[current] = saved_spots[this_square]+1

            if(0<=(this_square[0]-item[0])<n):
                if(0<=(this_square[1]+item[1])<n):
                    current = (this_square[0]-item[0], this_square[1]+item[1])
                    if(current not in saved_spots):
                        queue.append(current)
                        saved_spots[current] = saved_spots[this_square]+1
                if(0<=(this_square[1]-item[1])<n):
                    current = (this_square[0]-item[0], this_square[1]-item[1])
                    if(current not in saved_spots):
                        queue.append(current)
                        saved_spots[current] = saved_spots[this_square]+1

            if(0<=(this_square[0]+item[1])<n):
                if(0<=(this_square[1]+item[0])<n):
                    current = (this_square[0]+item[1], this_square[1]+item[0])
                    if(current not in saved_spots):
                        queue.append(current)
                        saved_spots[current] = saved_spots[this_square]+1
                if(0<=(this_square[1]-item[0])<n):
                    current = (this_square[0]+item[1], this_square[1]-item[0])
                    if(current not in saved_spots):
                        queue.append(current)
                        saved_spots[current] = saved_spots[this_square]+1

            if(0<=(this_square[0]-item[1])<n):
                if(0<=(this_square[1]+item[0])<n):
                    current = (this_square[0]-item[1], this_square[1]+item[0])
                    if(current not in saved_spots):
                        queue.append(current)
                        saved_spots[current] = saved_spots[this_square]+1
                if(0<=(this_square[1]-item[0])<n):
                    current = (this_square[0]-item[1], this_square[1]-item[0])
                    if(current not in saved_spots):
                        queue.append(current)
                        saved_spots[current] = saved_spots[this_square]+1
            if((n-1, n-1) in saved_spots.keys()):
                break
        #print(saved_spots)
        if((n-1, n-1) in saved_spots.keys()):
            min_moves.append(saved_spots[(n-1, n-1)])
        else:
            min_moves.append(-1)

    new_min_moves = []
    output_str = ""
    for i in range(1, n):
        new_min_moves.append([min_moves[0:n-1]])
        output_str+=(' '.join([str(l) for l in min_moves[0:n-1]]))+"\n"
        min_moves = min_moves[n-1:]

    return output_str


print(knightlOnAChessboard(5))
