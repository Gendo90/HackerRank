import math
import os
import random
import re
import sys


# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    #basic map implementation problem
    bird_ids = {}
    for bird in arr:
        if(bird in bird_ids):
            bird_ids[bird]+=1
        else:
            bird_ids[bird]=1

    #get the maximum frequency and then find all birds seen at that frequency
    max_freq = max(bird_ids.values())
    most_spotted_birds = [bird for bird in bird_ids.keys() if bird_ids[bird]==max_freq]
    most_spotted_birds.sort()

    return most_spotted_birds[0]


print(migratoryBirds([1,1,2,2,3])
