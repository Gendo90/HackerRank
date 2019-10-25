#!/bin/python3

import math
import os
import random
import re
import sys

# Make the class "Graph"
class Graph(object):
    def __init__(self, n):
        self.size = n
        self.graph_map = {}
        for i in range(1, n+1):
            self.graph_map[i] = set()

    def connect(self, a, b):
        self.graph_map[a].add(b)
        self.graph_map[b].add(a)

    def find_all_distances(self, s):
        seen = {}
        seen[s] = 0
        queue = [s]
        #perform bfs to populate the "seen" map that contains the distances
        #of the nodes from the start node for all connected nodes
        while(queue):
            curr = queue.pop(0)
            for item in self.graph_map[curr]:
                if(item not in seen):
                    queue.append(item)
                    seen[item] = seen[curr] + 6

        #populate the output array as required by the specs
        output = []
        for i in range(1, n+1):
            if(seen.get(i)):
                output.append(seen[i])
            else:
                output.append(-1)
        #remove "source" node from list
        output.pop(s-1)
        print(" ".join(map(str, output)))
        return output
