#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    seen_brackets = []
    complements = {'[':']', '{':'}', '(':')'}

    for item in s:
        if(item in complements):
            seen_brackets.append(item)
        elif(seen_brackets):
            if(item!=complements[seen_brackets.pop()]):
                return "NO"
        else:
            return "NO"

    if(not seen_brackets):
        return "YES"
    else:
        return "NO"

# print(isBalanced("{[()]}"))
# print(isBalanced("{[()]}"))
# print(isBalanced("{[(])}"))
# print(isBalanced("{{[[(())]]}}"))
# print(isBalanced("}][}}(}][))]"))
# print(isBalanced("[](){()}"))
# print(isBalanced("()"))
# print(isBalanced("({}([][]))[]()"))
# print(isBalanced("{)[](}]}]}))}(())("))
# print(isBalanced("([[)"))
# print(isBalanced("))"))
