#!/bin/python3

import os
import sys
import numpy as np

#
# Complete the equalStacks function below.
#
def twoStacks(x, a, b):
    #first reverse arrays to pop from end!
    a = a[::-1]
    b = b[::-1]
    #try dynamic programming (store all values of blocks that can be removed?)
    num_removed_first = [0]
    curr_total = 0

    go_back_a = []
    go_back_b = []

    while(curr_total<=x and a):
        go_back_a.append(a.pop())
        # print(go_back_a)
        curr_total+=go_back_a[-1]
        if(curr_total<=x):
            num_removed_first.append(num_removed_first[-1]+1)
        else:
            a.append(go_back_a.pop())
            curr_total-=a[-1]
            break

    num_removed_second = [0, num_removed_first[-1]]
    copy_first_num_removed = num_removed_first[:-1]

    while(go_back_a):
        a.append(go_back_a.pop())
        curr_total-=a[-1]
        num_removed_second.append(num_removed_second[-1]-1)
        while(curr_total<=x and b):
            # print(curr_total, go_back_a, b, num_removed_second)
            go_back_b.append(b.pop())
            curr_total+=go_back_b[-1]
            if(curr_total<=x):
                num_removed_second.append(num_removed_second[-1]+1)
            else:
                b.append(go_back_b.pop())
                curr_total-=b[-1]
                break


    first_max = max(max(num_removed_first), max(num_removed_second))

    #restart for b down and then back!
    curr_total = 0
    num_removed_third = [0]

    while(go_back_b):
        b.append(go_back_b.pop())

    while(curr_total<=x and b):
        go_back_b.append(b.pop())
        # print(go_back_b)
        curr_total+=go_back_b[-1]
        if(curr_total<=x):
            num_removed_third.append(num_removed_third[-1]+1)
        else:
            b.append(go_back_b.pop())
            curr_total-=b[-1]
            break

    # print(go_back_b, num_removed_third)
    num_removed_fourth = [0, num_removed_third[-1]]
    copy_third_num_removed = num_removed_third[:-1]

    while(go_back_b):
        b.append(go_back_b.pop())
        curr_total-=b[-1]
        num_removed_fourth.append(num_removed_fourth[-1]-1)
        while(curr_total<=x and a):
            # print(curr_total, go_back_a, b, num_removed_fourth)
            go_back_a.append(a.pop())
            curr_total+=go_back_a[-1]
            if(curr_total<=x):
                num_removed_fourth.append(num_removed_fourth[-1]+1)
            else:
                a.append(go_back_a.pop())
                curr_total-=a[-1]
                break

    # print(num_removed_third, num_removed_fourth)

    second_max = max(max(num_removed_third), max(num_removed_fourth))

    #find the max number of blocks removed from first and second parts
    return max(first_max, second_max)












    #attempt greedy algorithm - try to remove smallest integer on top each time
    #greedy algorithm did not work
    # curr_total = 0
    # num_removed = 0
    # while(curr_total<=x and (a or b)):
    #     # print(a, b)
    #     if(a and b):
    #         if(a[0]>b[0]):
    #             curr_total+=b.pop(0)
    #         else:
    #             curr_total+=a.pop(0)
    #     elif (a==[]):
    #         curr_total+=b.pop(0)
    #     else:
    #         curr_total+=a.pop(0)
    #     num_removed+=1
    #
    # if(not (a or b)):
    #     return num_removed
    # else:
    #     return num_removed-1


#
# arr1 = [7, 15, 12, 0, 5, 18, 17, 2, 10, 15, 4, 2, 9, 15, 13, 12, 16]
#
# arr2 = [12, 16, 6, 8, 16, 15, 18, 3, 11, 0, 17, 7, 6, 11, 14, 13, 15, 6, 18, 6, 16, 12, 16, 11, 16, 11]
#
# print(twoStacks(62, arr1, arr2))



# x=71
# arr1 = [14, 8, 17, 1, 16, 10, 0, 12, 0, 15, 13, 4, 11, 2, 14, 7, 11, 0, 9, 17, 8, 0, 16, 4, 7, 15, 7, 8, 11, 10, 18, 6, 19, 16, 7]
# arr2 = [7, 18, 0, 19]
#
# print(twoStacks(71, arr1, arr2))

# x= 87
# arr1 = [10, 12, 15, 3, 19, 12, 13, 12, 15, 1, 18, 18]
# arr2 = [2, 19, 16, 16, 7, 12, 10, 9, 2, 16, 12, 1, 0, 3, 3, 3, 16, 8, 2, 6, 12, 17, 2]
#
# print(twoStacks(x, arr1, arr2))

#
# x= 19
# arr1 = [14, 0, 15, 12, 15, 6]
# arr2 = [2, 2, 6, 9, 0, 1, 1, 18]
#
# print(twoStacks(x, arr1, arr2))


# x=58
# arr1 = [9, 15, 19, 19, 6, 6, 8, 7, 7, 14, 3, 15, 0]
# arr2 = [11, 8, 6, 7, 0, 17, 10, 5, 11, 11]
#
# print(twoStacks(x, arr1, arr2))

if __name__ == '__main__':
    # arr = np.genfromtxt(r'twoStacks_test_input.txt', delimiter='\n')
    # Open file

    fileHandler = open("twoStacks_test_input.txt", "r")

    # Get list of all lines in file
    listOfLines = fileHandler.readlines()

    # Close file
    fileHandler.close()

    input_lines = []
    for line in listOfLines:
        input_lines.append(line.strip())

    # print(input_lines)

    for game in range(0, int(input_lines[0])):

        first = list(map(int, input_lines[3*game+1].rstrip().split()))[2]

        a = list(map(int, input_lines[3*game+2].rstrip().split()))

        b = list(map(int, input_lines[3*game+3].rstrip().split()))

        print(twoStacks(first, a, b))

        # arr = [3, 1, 2, 4, 7]
        # print(sort_and_count_inversions(arr)[0])
