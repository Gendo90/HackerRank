#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#
def specialBFS(start, color, ids, graph, first=True, seen={}):
    #min distance given here is higher than any possible value - will be overwritten
    #by the first pairing of colors
    min_dist = 2000000000
    #count represents the distance between the source node and the subsequent
    #nodes found by each "search" wave from the source
    count = 0
    queue = [(start, count)]
    while(queue):
        (curr, curr_count) = queue.pop(0)
        count+=1
        additional_items = [(a, count) for a in graph[curr] if a not in seen]
        queue.extend(additional_items)
        seen[curr] = True
        #need to recursively search all items next to this item when the correct color is found!
        if(ids[curr-1]==color and first):
            for item in graph[curr]:
                #note that the map of "seen" items does not include all the items seen - otherwise
                #would have problems back-tracking if already covered nodes that were the
                #shortest path to the next node with this color (see example 2 given on line 62 of this file)
                this_dist, this_seen = specialBFS(item, color, ids, graph, False, {curr:True})
                #prevents the algorithm from taking too long, only looking at territory covered
                #between the correct colors once!
                seen.update(this_seen)
                #add one because the count starts at 0, so represents the first link
                #from the source to its adjacent item
                min_dist = min(this_dist+1, min_dist)
        elif(ids[curr-1]==color and not first):
            #found the second item of the pairing, closest in this case!
            #return all items "seen" between them so they are not searched again
            return curr_count, seen

    return min_dist, seen

def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    #case where no pairing is found - only one or less value of that color!
    if(ids.count(val)<2):
        return -1
    # solve here
    graph_map = {}
    for i in range(1, len(ids)+1):
        graph_map[i] = set()

    for item in zip(graph_from, graph_to):
        graph_map[item[0]].add(item[1])
        graph_map[item[1]].add(item[0])

    #implement bfs that gets interrupted by finding like colors
    return specialBFS(1, val, ids, graph_map)[0]


print(findShortest(5, [1,1,2,3], [2,3,4,5], [1,2,3,3,2], 2))


# if __name__ == '__main__':
#     roadsAndLibraries(5, 6, 1, [[1, 2], [1, 3], [1, 4]])
#
#     print(result)
