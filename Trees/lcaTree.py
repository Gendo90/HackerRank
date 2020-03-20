#!/bin/python3

import math
import os
import random
import re
import sys

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

#get node of a lowest common ancestor (lca) of two nodes
#careful with this function, need to switch from returning lists to
#returning the correct node (the lca) at some point during the recursion!
def lca(root, v1, v2, descendants=[]):
  #recursive, with a trace of descendants
  if(not root):
      return []

  leftChild = root.left
  rightChild = root.right
  #case where left child search found the LCA
  leftResult = lca(leftChild, v1, v2, descendants)
  if(isinstance(leftResult, Node)):
      return leftResult

  #case where the right child search found the LCA
  rightResult = lca(rightChild, v1, v2, descendants)
  if(isinstance(rightResult, Node)):
      return rightResult


  descendants = descendants+ leftResult + rightResult + [root]
  check = list(map(lambda x: x.info, descendants))
  # print(v1, v2, check)

  #identify the LCA
  if(v1 in check and v2 in check):
      return root
  else:
      return descendants


tree = BinarySearchTree()
t = 8

arr = [8, 4, 9, 1, 2, 3, 6, 5]

for i in range(t):
    tree.create(arr[i])

# v = list(map(int, input().split()))

ans = lca(tree.root, 1, 2)
print (ans.info)
