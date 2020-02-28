#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bfs function below.
def bfs(n, m, edges, s):
    #initialize graph
    graph = {}
    for i in range(1, n+1):
        graph[i] = set()

    for edge_from, edge_to in edges:
        graph[edge_to].add(edge_from)
        graph[edge_from].add(edge_to)

    #perform bfs
    queue = [(s, 0)]
    seen = {}
    while(queue):
        curr = queue.pop(0)
        seen[curr[0]] = curr[1]
        for node in graph[curr[0]]:
            if(node not in seen):
                queue.append((node, curr[1]+6))
                seen[node] = curr[1]+6

    #now output the answer, with formatting
    output_arr = []
    for i in range(1, n+1):
        if(i==s):
            continue
        if(i in seen):
            output_arr.append(seen[i])
        else:
            output_arr.append(-1)

    return output_arr

print(bfs(4, 2, [[1, 2], [1, 3]], 1))
