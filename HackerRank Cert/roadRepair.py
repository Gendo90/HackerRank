#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getMinCost' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY employee_id
#  2. INTEGER_ARRAY job_id
#

def getMinCost(employee_id, job_id):
    ordered_employees = sorted(employee_id)
    ordered_jobs = sorted(job_id)
    total_dist = 0

    for i in range(len(employee_id)):
        total_dist+=abs(ordered_jobs[i]-ordered_employees[i])

    return total_dist
