#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    a_in_s = s.count("a")
    complete_repeats, remainder = divmod(n, len(s))
    total_as = complete_repeats*a_in_s + (s[0:remainder]).count("a")

    return total_as

print(repeatedString("aba", 10))
