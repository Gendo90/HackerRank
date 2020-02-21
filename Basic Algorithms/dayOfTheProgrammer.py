#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    leap_year_date = {True: "12.09.", False:"13.09."}
    is_leap_year = False
    if(year<1918):
        if(year%4==0):
            is_leap_year = True
    elif(year==1918):
        return "26.09.1918"
    else:
        if((year%400==0) or (year%4==0 and not year%100==0)):
            is_leap_year = True

    return leap_year_date[is_leap_year]+str(year)


print(dayOfProgrammer(2016))
print(dayOfProgrammer(2017))
