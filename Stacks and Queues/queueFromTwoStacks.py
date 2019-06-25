#!/bin/python3

import math
import os
import random
import re
import sys

#Tricky to notice that the stack reverses the order, and that you need to keep
# adding to the other side and popping from the reversed side (not just
# popping a single element and then popping into the other stack, or adding
# items will mess up the order)

# Complete the maxElement function below.
def headElement(s):
    first_stack = []
    second_stack = []
    this_head = 0
    second_stack_has_head = False
    for query in s:
        if(query[0]==1):
            if(not second_stack and not first_stack):
                second_stack.append(query[1])
                this_head = second_stack[0]
                second_stack_has_head = True
            elif(second_stack_has_head):
                first_stack.append(query[1])
            elif(first_stack):
                second_stack.append(query[1])
        elif(query[0]==2):
            if(second_stack_has_head):
                l = second_stack.pop()
                if(second_stack):
                    this_head = second_stack[-1]
            else:
                l = first_stack.pop()
                if(first_stack):
                    this_head = first_stack[-1]
            if(second_stack_has_head and not second_stack and first_stack):
                for i in range(len(first_stack)):
                    second_stack.append(first_stack.pop())
                this_head = second_stack[-1]
                second_stack_has_head = True
            elif(not first_stack and second_stack and not second_stack_has_head):
                for i in range(len(second_stack)):
                    first_stack.append(second_stack.pop())
                this_head = first_stack[-1]
                second_stack_has_head = False
        else:
            print(this_head)
        print(first_stack, second_stack)



n = int(input())

total_arr = []
for i in range(n):
    arr = input()
    if(len(arr)>1):
        arr = arr.split(" ")
        arr = [int(a) for a in arr]
    else:
        arr = [int(a) for a in arr]
    total_arr.append(arr)

headElement(total_arr)
