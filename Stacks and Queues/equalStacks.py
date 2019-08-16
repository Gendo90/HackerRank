#!/bin/python3

import os
import sys

#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    #keep removing largest element from the top, then see the closest a stack can
    #get and be higher, then remove largest element again, etc.
    #look at only two stacks at once, then look at the third stack to see if
    #it is also has a height of that value
    total_first_height = sum(h1)
    total_second_height = sum(h2)
    total_third_height = sum(h3)

    while(not (total_first_height==total_second_height and total_first_height==total_third_height)):
        # print(total_first_height, total_second_height)
        if(total_first_height>total_second_height):
            total_first_height -= h1.pop(0)
        elif(total_first_height<total_second_height):
            total_second_height -= h2.pop(0)
        else:
            #check if the third stack has an equal value here!
            while(total_third_height>total_first_height):
                total_third_height -= h3.pop(0)
            # print(total_first_height, total_third_height)
            if(total_third_height==total_first_height):
                return total_third_height
            else:
                total_first_height -= h1.pop(0)

    return total_first_height


arr1 = [3, 2, 1, 1, 1]
arr2 = [4, 3, 2,]
arr3 = [1, 1, 4, 1]

print(equalStacks(arr1, arr2, arr3))
