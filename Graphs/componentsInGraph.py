#!/bin/python3

import os
import sys
import numpy as np

#
# Complete the componentsInGraph function below.
#
def componentsInGraph(gb):
    components = {}
    reverse_value_lookup = {}
    for edge in gb:
        if(edge[0] in components and reverse_value_lookup.get(edge[1])==edge[0]):
            continue
        elif(edge[0] not in components and edge[0] not in reverse_value_lookup
            and edge[1] not in reverse_value_lookup):
            components[edge[0]] = [edge[1]]
            reverse_value_lookup[edge[1]] = edge[0]
        elif(edge[0] in reverse_value_lookup and edge[1] not in reverse_value_lookup):
            ind = reverse_value_lookup[edge[0]]
            components[ind].append(edge[1])
            reverse_value_lookup[edge[1]] = ind
        elif(edge[0] in components):
            if(reverse_value_lookup.get(edge[1])):
                #combine these components
                conn_component = reverse_value_lookup[edge[1]]
                components[edge[0]].extend(components[conn_component])
                components[edge[0]].append(conn_component)
                former_vals = components.pop(conn_component)
                #replace pointers for all values in former item
                for item in former_vals:
                    reverse_value_lookup[item] = edge[0]
                #re-route lookups for components containing the former first
                #vertex
                reverse_value_lookup[conn_component] = edge[0]
            else:
                components[edge[0]].append(edge[1])
                reverse_value_lookup[edge[1]] = edge[0]
        elif(edge[1] in reverse_value_lookup):
            if(reverse_value_lookup.get(edge[0])):
                #double check this logic! should just be edge[0] or get(edge[0])???
                if(reverse_value_lookup.get(edge[0])!=reverse_value_lookup[edge[1]]):
                    #combine these components
                    conn_component = reverse_value_lookup[edge[1]]
                    add_index = reverse_value_lookup[edge[0]]
                    components[add_index].extend(components[conn_component])
                    components[add_index].append(conn_component)
                    former_vals = components.pop(conn_component)
                    #replace pointers for all values in former item
                    for item in former_vals:
                        reverse_value_lookup[item] = add_index
                    #re-route lookups for components containing the former first
                    #vertex
                    reverse_value_lookup[conn_component] = add_index
                else:
                    routed_comp = reverse_value_lookup[edge[0]]
                    if(edge[1] not in components[routed_comp]):
                        components[routed_comp].append(edge[1])
                        reverse_value_lookup[edge[1]] = routed_comp
            else:
                ind = reverse_value_lookup[edge[1]]
                components[ind].append(edge[0])
                reverse_value_lookup[edge[0]] = ind
        # print(edge, components, reverse_value_lookup)

    #need to remove all node that refer to themselves???
    # print(components, reverse_value_lookup)

    #find min and max lengths of arrays in components to find min and max vertices
    val_lengths = [len(arr) for arr in components.values()]
    min_vertices = min(val_lengths)+1
    max_vertices = max(val_lengths)+1

    return min_vertices, max_vertices


if __name__ == '__main__':
    # n = int(input())
    fileHandler = open("test_case_1.txt", "r")

    # Get list of all lines in file
    listOfLines = fileHandler.readlines()

    # Close file
    fileHandler.close()
    print(listOfLines)

    gb = []
    for i, line in enumerate(listOfLines):
        if(i==0):
            continue
        gb.append(list(map(int, line.split())))
    print(gb)

    result = componentsInGraph(gb)

    print(result)
