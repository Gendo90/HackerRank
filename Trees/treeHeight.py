#!/bin/python3

import math
import os
import random
import re
import sys

#get height of a binary tree from the root node
def height(root):
    leftChild = root.left
    rightChild = root.right
    if(not leftChild and not rightChild):
        return 0

    leftHeight = 0
    if(leftChild):
        leftHeight += height(leftChild) + 1

    rightHeight = 0
    if(rightChild):
        rightHeight += height(rightChild) + 1

    return max(leftHeight, rightHeight)
