#!/bin/python3

import math
import os
import random
import re
import sys
import string

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    dict_a = {}
    dict_b = {}
    total_changes=0
    for letter in string.ascii_lowercase:
        dict_a[letter] = 0
        dict_b[letter] = 0

    for letter in a:
        dict_a[letter]+=1

    for letter in b:
        dict_b[letter]+=1

    for letter in string.ascii_lowercase:
        freq_a = dict_a[letter]
        freq_b = dict_b[letter]
        if(freq_a!=freq_b):
            total_changes+=(max(freq_a, freq_b)-min(freq_a, freq_b))

    return total_changes

print(makeAnagram("abc", "cde"))
print(string.ascii_lowercase)
