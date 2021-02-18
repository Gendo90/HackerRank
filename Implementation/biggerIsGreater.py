import math
import os
import random
import re
import sys
import string
import pandas as pd
from collections import defaultdict

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    #shift letters later in the alphabet before earlier letters
    #in string that are earlier in the alphabet
    alphabet = string.ascii_lowercase

    # w = "bpgqfwoyntuhkvwo"

    letter_map = defaultdict(int)
    num_map = defaultdict(str)

    for i, letter in enumerate(alphabet):
        letter_map[letter] = i
        num_map[i] = letter

    #convert the string to a numerical array of letter positions
    letter_arr = [letter_map[a] for a in w]

    #start from the rightmost letter, and insert that letter before the the rightmost letter
    #that is earlier in the alphabet before it

    #no, find the difference between that letter and the previous letters

    #use differences between letters as a new array
    #so that the insertion is the first change downward in position from
    #right to left, and is replaced with the next highest value already seen

    change_ind = len(w)-1
    lowest_val_seen = letter_arr[-1]
    lower_num_found = False
    for i in range(len(w)-1, 0, -1):
        if(letter_arr[i]> lowest_val_seen):
            lowest_val_seen = letter_arr[i]
        if(letter_arr[i-1] < lowest_val_seen):
            change_ind = i-1
            lower_num_found = True
            break

    if(not lower_num_found):
        return "no answer"

    #find min value that is greater than the earliest number in alphabet
    change_num = letter_arr[change_ind]
    min_diff = 100
    swap_ind = 0
    for i, letter in enumerate(letter_arr[change_ind+1:]):
        if(letter - change_num > 0 and min_diff > letter - change_num):
            swap_ind = i + change_ind + 1
            min_diff = letter-change_num

    # rightmost_letter = letter_arr[-1]
    # insert_ind = len(w)-1
    # letter_found = False
    # for l, letter in enumerate(letter_arr[::-1]):
    #     find_ind = len(w)-1-l
    #     for i in range(find_ind-1, -1, -1):
    #         if(letter_arr[i] < letter):
    #             insert_ind = i
    #             letter_found = True
    #             break
    #
    #     if(letter_found):
    #         break
    # else:
    #     return "no answer"

    #note that the string must be sorted after the swap index
    #to minimize the lexical size
    insert_value = letter_arr.pop(swap_ind)
    letter_arr.insert(change_ind, insert_value)
    # if(insert_ind == 0):
    letter_arr[change_ind+1:] = sorted(letter_arr[change_ind+1:])

    output = [num_map[a] for a in letter_arr]

    return "".join(output)


print(biggerIsGreater("dcba"))

# input_data = pd.read_csv("input03_bigger_is_Greater.txt")
#
# my_results = input_data.copy()
#
# my_results["100"] = my_results["100"].apply(biggerIsGreater)
#
# expected_results = pd.read_csv("output03_bigger_is_Greater.txt")
#
# check_df = (my_results != expected_results)
#
# print(check_df.loc[check_df['100'] == True])
