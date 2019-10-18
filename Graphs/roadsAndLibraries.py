#!/bin/python3

import math
import os
import random
import re
import sys

def bfs(start, graph):
    seen = {}
    queue = [start]
    while(queue):
        curr = queue.pop(0)
        if(curr not in seen):
            this_node_list = [item for item in graph[curr] if (item not in seen)]
            queue.extend(this_node_list)
            seen[curr] = True
    return seen

# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    #case where the libraries are the same or cheaper to build in each city
    #instead of connecting them by roads
    if(c_lib<=c_road):
        return n*c_lib

    graph_map = {}
    all_seen = {}
    all_connected = {}
    #build graph
    for i in range(1, n+1):
        graph_map[i] = set()

    for edge in cities:
        graph_map[edge[0]].add(edge[1])
        graph_map[edge[1]].add(edge[0])

    for i in range(1, n+1):
        if(i not in all_seen):
            this_seen = bfs(i, graph_map)
            all_seen.update(this_seen)
            all_connected[i] = this_seen

    road_list = [len(all_connected[a])-1 for a in all_connected.keys()]
    num_roads = sum(road_list)
    num_libraries = len(all_connected.keys())
    # print(num_roads, num_libraries)

    total = num_roads*c_road+num_libraries*c_lib

    return total

print(roadsAndLibraries(5, 6, 1, [[1, 2], [1, 3], [1, 4]]))


# if __name__ == '__main__':
#     roadsAndLibraries(5, 6, 1, [[1, 2], [1, 3], [1, 4]])
#
#     print(result)
