#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.
def angryProfessor(k, a):
    #only keep values of a that are 0 or less
    on_time_students = [student for student in a if(student<=0)]
    #need at least k students to be on time
    if(len(on_time_students)>=k):
        return "NO"
    else:
        return "YES"


# print(migratoryBirds([1,1,2,2,3])
