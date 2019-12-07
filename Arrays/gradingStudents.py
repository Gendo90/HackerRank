#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#
def higher_mult(grade):
    if(grade%5==0):
        return grade
    else:
        return (5*(grade//5)+5)

def gradingStudents(grades):
    output_arr = []
    for grade in grades:
        if(grade>=38):
            diff = (higher_mult(grade)-grade)
            if(diff<=2):
                grade+=diff
        output_arr.append(grade)

    return output_arr
