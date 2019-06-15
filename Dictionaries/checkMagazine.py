#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazine_words = {}
    for item in magazine:
        if(item not in magazine_words):
            magazine_words[item]=1
        else:
            magazine_words[item]+=1

    for word in note:
        if(word not in magazine_words):
            print("No")
            return
        elif(magazine_words[word]==0):
            print("No")
            return
        else:
            magazine_words[word]-=1

    print("Yes")
