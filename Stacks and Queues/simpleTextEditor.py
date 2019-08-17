#!/bin/python3

import os
import sys

#
# Complete the simpleTextEditor function below.
#
def simpleTextEditor(operation, val, s="", state=[""]):
    if(operation==1):
        s+=val
        state.append(s)
    elif(operation==2):
        k = int(val)
        s=s[:len(s)-k]
        state.append(s)
    elif(operation==3):
        k = int(value)-1
        print(s[k])
    else:
        state.pop()
        s = state[-1]

    return s, state


if __name__ == '__main__':

    s = ""
    state = [""]
    value=""

    total_ops = int(input())

    for operation in range(total_ops):
        input_arr = input().split(" ")
        op = int(input_arr[0])
        if(op!=4):
            value = input_arr[1]
        s, state = simpleTextEditor(op, value, s, state)
