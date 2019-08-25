#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtHead(head, data):
    node = SinglyLinkedListNode(data)
    node.next = head
    head = node

    return head




# if __name__ == '__main__':
#     # n = int(input())
#     fileHandler = open("insertTailNode_test_case.txt", "r")
#
#     # Get list of all lines in file
#     listOfLines = fileHandler.readlines()
#
#     # Close file
#     fileHandler.close()
#
#     llist = SinglyLinkedList()
#
#     gb = []
#     for i, line in enumerate(listOfLines):
#         if(i==0):
#             continue
#         gb.append(int(line))
#
#     print(sys.getrecursionlimit())
#     #note had to change the recursion limit here to get it to work!
#     sys.setrecursionlimit(5000)
#
#     for i in range(len(gb)):
#         llist_item = gb[i]
#         llist_head = insertNodeAtTail(llist.head, llist_item)
#         llist.head = llist_head
#
#     node = llist.head
#     while(node):
#         print(node.data)
#         node = node.next
