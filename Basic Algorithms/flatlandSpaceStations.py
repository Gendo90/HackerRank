#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    max_dist = 0
    curr_space_station_ind = 0
    num_space_stations = len(c)
    #sort the array containing cities with space stations
    c.sort()

    for city in range(n):
        if(city<c[curr_space_station_ind]):
            if(curr_space_station_ind>0):
                curr_distance = min(c[curr_space_station_ind] - city, city - c[curr_space_station_ind-1])
            else:
                curr_distance = c[curr_space_station_ind] - city
        else:
            curr_distance = city-c[curr_space_station_ind]

        if(city==c[curr_space_station_ind]):
            curr_distance = 0
            #only line of conditional logic that I missed!
            if(curr_space_station_ind<num_space_stations-1):
                curr_space_station_ind+=1

        if(max_dist<curr_distance):
            max_dist = curr_distance

    return max_dist

print(flatlandSpaceStations(5, [0, 4]))
print(flatlandSpaceStations(6, [0, 1, 2, 4, 3, 5]))
print(flatlandSpaceStations(20, [13, 1, 11, 10, 6]))
