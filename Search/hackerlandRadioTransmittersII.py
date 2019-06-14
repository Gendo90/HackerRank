#!/bin/python3

import math
import os
import random
import re
import sys

# helper function to find index of next house not covered
def houseUncoveredIndex(minValue, houses):
    for i, item in enumerate(houses):
        if(item>(minValue)):
            return i

    return -1


# Complete the hackerlandRadioTransmitters function below.
def hackerlandRadioTransmitters(x, k):
    #greedy algorithm
    #first sort x
    x.sort()
    transmitter_locs = []
    houses_left = x[:]
    # print(houses_left)
    i=0
    # place transmitter so first house is covered at edge (e.g. if transmitter
    # placed at next house would not be covered)
    while(houses_left):
        if(i>len(houses_left)-1):
            transmitter_locs.append(i-1)
            break

        if(houses_left[i]-(k)>houses_left[0]):
            transmitter_locs.append(i-1)
            # house that is outside of the transmitter range on the right
            n=i-1
            while(houses_left[n]==houses_left[i]):
                if(n==0):
                    break
                n-=1
            # houses_left = [a for a in houses_left if a>(houses_left[n]+(k))]
            housesIndex = houseUncoveredIndex((houses_left[n]+(k)), houses_left)
            if(housesIndex!=-1):
                houses_left = houses_left[housesIndex:]
            else:
                transmitter_locs.append(i-1)
                break
            if(houses_left==[]):
                break
            i=0
        i+=1

    return len(transmitter_locs)

print(hackerlandRadioTransmitters([7, 2, 4, 6, 5, 9, 12, 11], 2))
