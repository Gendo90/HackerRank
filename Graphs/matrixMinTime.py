#!/bin/python3

import math
import os
import random
import re
import sys
import time

def bfs(start, graph, machine_map):
    queue = [(start, 0)]
    seen = {start:True}

    while(queue):
        curr = queue.pop(0)
        if(curr[0] in machine_map and curr[0]!=start):
            print(start, curr[0])
            return True
        for item in graph[curr[0]]:
            if(item not in seen):
                queue.append(item)
                seen[item] = True

    return False


def dijkstra_mapping(start, graph, machine_map):
    this_seen = {start:([(start, 0)])}
    path = [start]
    all_possible = {}
    count = 100

    while(((len(path)==1 and graph[start]) or path[-1] not in machine_map)):
        time_limit = 10000000
        for node in this_seen.keys():
            for cityto, time in graph[node]:
                this_path = sum(unzip_together(this_seen[node]))+time
                if(cityto in this_seen and sum(unzip_together(this_seen[cityto]))<=this_path):
                    if(cityto in this_seen and not cityto in this_seen[cityto]):
                        continue
                    else:
                        #remove cycles
                        print("found itself")
                if(this_path<time_limit):
                    time_limit = this_path
                    next_city = cityto
                    last_city = node
                    cut_time = time
        # print(this_seen.values())
        # print(all_possible.values())
        all_possible = this_seen.copy()
        path.append(next_city)
        # print(graph)
        this_seen[next_city] = this_seen[last_city][:]
        this_seen[next_city].append((next_city, cut_time))
        if(all_possible==this_seen):
            count-=1
            if(count<0):
            # print(all_possible, this_seen)
            # print("oh no", flush=True)
                print("skipped", start)
                return [1], [1], [0]
        # print(this_seen)

    return path, this_seen[path[-1]], path[-1]

def sorter_func(x):
    return x[1]

def unzip_together(x):
    a=[]
    for i in x:
        a.append(i[1])
    return a

# Complete the minTime function below.
#calc shortest path to next machine, then cut the smallest edge of that path
#so first implement dijkstra's algorithm (greedy, keep selecting min path)
def minTime(roads, machines):
    graph_map = {}
    machine_map = {}
    time_total = 0
    for machine in machines:
        machine_map[machine] = True

    for item in range(len(roads)+1):
        graph_map[item] = set()

    for city1, city2, time in roads:
        graph_map[city1].add((city2, time))
        graph_map[city2].add((city1, time))

    for city in machine_map.keys():
        path, times, curr = dijkstra_mapping(city, graph_map, machine_map)
        # print(times)
        # print(graph_map)
        starter = times.pop(0)
        #need to sever the connection here at the minimum edge
        times.sort(key=sorter_func)
        if(not times):
            continue
        removal = times[0]
        # print(removal)
        times.append(starter)
        second_removal_list = [a for a in graph_map[removal[0]] if (a[0] in list(zip(*times))[0] and a[1]==removal[1])]
        second_removal = second_removal_list.pop()
        graph_map[removal[0]].remove(second_removal)
        graph_map[second_removal[0]].remove(removal)
        # print(city, removal[1], flush=True)

        time_total+=removal[1]

    #gives remaining items to be disconnected
    print(graph_map)
    print(machine_map)
    for item in machine_map.keys():
        if(bfs(item, graph_map, machine_map)):
            path, times, curr = dijkstra_mapping(item, graph_map, machine_map)
            # print(times)
            # print(graph_map)
            starter = times.pop(0)
            #need to sever the connection here at the minimum edge
            times.sort(key=sorter_func)
            if(not times):
                continue
            removal = times[0]
            # print(removal)
            times.append(starter)
            second_removal_list = [a for a in graph_map[removal[0]] if (a[0] in list(zip(*times))[0] and a[1]==removal[1])]
            second_removal = second_removal_list.pop()
            graph_map[removal[0]].remove(second_removal)
            graph_map[second_removal[0]].remove(removal)
            # print(city, removal[1], flush=True)

            time_total+=removal[1]

    return time_total

# r = [(2, 1, 8), (1, 0, 5), (2, 4, 5), (1, 3, 4)]
# k = [2, 4, 0]
# print(minTime(r, k))
#
# r = [(0, 1, 4), (1, 2, 3), (1, 3, 7), (0, 4, 2)]
# k = [2, 3, 4]
# print(minTime(r, k))
#
if __name__ == '__main__':

    fileHandler = open("minTime_TestCase2.txt", "r")

    # Get list of all lines in file
    listOfLines = fileHandler.readlines()

    # Close file
    fileHandler.close()

    n, k = map(int, listOfLines[0].split())

    roads = []

    for _ in range(1, n):
        roads.append(list(map(int, listOfLines[_].rstrip().split())))
    # print(roads)

    machines = []

    for _ in listOfLines[n:]:
        machines_item = int(_)
        machines.append(machines_item)

    print(machines)

    #expected to be 610
    #closer, now get 528
    print(minTime(roads, machines))
