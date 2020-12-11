#!/bin/python3

import os
import sys
import numpy as np

#
# Complete the equalStacks function below.
#
def twoStacks(x, a, b):
    #make stacks reversed - pop from start, not end
    a.reverse()
    b.reverse()

    #first remove all possible blocks from a
    a_removed = []
    total = 0
    count = 0
    all_counts = []
    a_size = len(a)
    a_size_orig = a_size

    b_removed = []
    b_size = len(b)
    b_size_org = b_size

    #try to go down as far as possible in 'a' stack only
    while(total<=x and a_size>0):
        curr = a.pop()
        a_removed.append(curr)
        total += curr
        count += 1
        a_size -= 1
    else:
        if(total>x):
            #backtrack one tile to keep x in check
            #may be used in next loop, actually
            # curr = a_removed.pop()
            # a.append(curr)
            # total -= curr
            # count -= 1
            # a_size += 1
            all_counts.append(count-1)
        # elif(total<x and a_size == 0):
        #     if(sum(b) + total <= x):
        #         return len(b) + a_size_orig
            #get all values possible on other stack, b
            #do not return answer(b may be larger than a - might have more tiles removed from b and some of a), because a is empty and the
            #running total can still increase
        elif(total == x):
            all_counts.append(count)
        elif(total < x):
            all_counts.append(count)
            while(total <= x and b_size > 0):
            #start going down the other stack
                b_curr = b.pop()
                b_removed.append(b_curr)
                total += b_curr
                b_size -= 1
                count += 1
            else:
                if(total <= x):
                    return a_size_orig + b_size_org
                elif(total > x):
                    b_curr = b_removed.pop()
                    b.append(b_curr)
                    total -= b_curr
                    b_size += 1
                    count -= 1
                    all_counts.append(count)

    #normal case to proceed - need to add one tile back at a time, and then
    #go down the "b" stack
    while(a_size != a_size_orig and b_size > 0):
        curr = a_removed.pop()
        a.append(curr)
        total -= curr
        count -= 1
        a_size += 1
        while(total <= x and b_size > 0):
            b_curr = b.pop()
            b_removed.append(b_curr)
            b_size -= 1
            total += b_curr
            count += 1
        else:
            if(total > x):
                #backtrack one tile, add to all counts
                b_curr = b_removed.pop()
                b.append(b_curr)
                b_size += 1
                total -= b_curr
                count -= 1
                all_counts.append(count)
            elif(b_size == 0):
                #cannot increase count any more (only add more 'a' stack tiles back)
                all_counts.append(count)
                #output max count
                return max(all_counts)
            elif(total == x):
                all_counts.append(count)


    return max(all_counts)












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

    fileHandler = open("twoStacks_test_input2.txt", "r")

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

        # print(first, a, b)

        print(twoStacks(first, a, b))

        # arr = [3, 1, 2, 4, 7]
        # print(sort_and_count_inversions(arr)[0])
