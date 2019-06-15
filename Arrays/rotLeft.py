#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    # complete_cycles, actual_shift = divmod(len(a), d)
    outputArray = a[d:]+a[0:d]
    return outputArray

print(rotLeft(list(range(5)), 4))
