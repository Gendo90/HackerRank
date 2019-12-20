#!/bin/python

import math
import os
import random
import re
import sys

def binary_search(input_array, value):
    test_array = input_array
    current_index = len(input_array)//2
    input_index = current_index

    found_value = test_array[current_index]
    while(len(test_array)>1 and found_value!=value):
        if(found_value<value):
            test_array = test_array[current_index:]
            current_index = len(test_array)//2
            input_index += current_index
            found_value = input_array[input_index]
        else:
            test_array = test_array[0:current_index]
            current_index = len(test_array)//2
            # divmod needed to be used instead of round() since the behavior
            # for .5 changed from rounding up to rounding down in Python 3
            q, r = divmod(len(test_array), 2.0)
            input_index = int(input_index - q - r)
            found_value = input_array[input_index]
    else:
        if(found_value==value):
            return input_index

    return input_index

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    #first, make a hash map of the scores and how many players are at each
    #score
    scores.sort(reverse=True)
    backwards = scores[:]
    backwards.sort()
    leaderboard = {1:[scores[0], 1]}
    scores_to_rank = {scores[0]:1}
    last = 1
    for item in scores[1:]:
        if(item==leaderboard[last][0]):
            leaderboard[last][1]+=1
        else:
            last+=1
            leaderboard[last] = [item, 1]
            scores_to_rank[item] = last

    #use binary search to find the equal or next highest score to Alice's,
    #and use the map to get the rank of that score to determine Alice's rank
    output = []
    for this_score in alice:
        score_index = binary_search(backwards, this_score)
        next_score = backwards[score_index]
        if(next_score==this_score):
            output.append(scores_to_rank[this_score])
        elif(next_score>this_score):
            output.append(scores_to_rank[next_score]+1)
        elif(next_score<this_score):
            output.append(scores_to_rank[next_score])

    return output
