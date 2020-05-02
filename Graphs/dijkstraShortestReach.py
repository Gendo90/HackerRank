#!/bin/python3

import math
import os
import random
import re
import sys
import time
import collections


#helper heap to be used to store edges for minimum spanning tree
class HeapMap():
    def __init__(self):
        self.indices = {}
        self.heap = []

    def push(self, elem):
        self.heap.append(elem)
        i=len(self.heap)
        #use lists instead of single values for the map from values to indices
        if(elem not in self.indices):
            self.indices[elem] = [i-1]
        else:
            self.indices[elem].append(i-1)
        #bubble-up through heap
        while(elem<self.heap[i//2-1] and i>1):
            #update map of values with new indices
            parent_elem = self.heap[i//2-1]
            self.indices[elem][-1] = i//2-1
            #need to replace the correct parent element index in the list
            #for multiple indices with the same value
            self.indices[parent_elem][self.indices[parent_elem].index(i//2-1)] = i-1
            #update element positions in heap array
            self.heap[i-1], self.heap[i//2-1] = self.heap[i//2-1], self.heap[i-1]
            i=i//2

    def popMin(self):
        result = self.heap.pop(0)
        #remove value from indices map if the minimum value is not -infinity
        if(result!=-float('inf')):
            if(len(self.indices[result])==1):
                self.indices.pop(result)
            else:
                self.indices[result].pop(self.indices[result].index(0))

        if(not self.heap):
            return result
        #get the length of the heap
        heap_size = len(self.heap)

        #replace first element with the last element in balanced heap
        last_elem = self.heap.pop()
        self.heap.insert(0, last_elem)
        self.indices[last_elem][self.indices[last_elem].index(heap_size)] = 0
        #bubble down through heap to get new minimum at position 0
        i=1
        while(i<heap_size):
            if(2*i<=heap_size):
                first_child_ind = 2*i-1
            else:
                break
            if(2*i+1<=heap_size):
                second_child_ind = 2*i
            else:
                second_child_ind=None
            #find the minimum child and its index in the heap to bubble down
            if(second_child_ind==None or self.heap[first_child_ind]<self.heap[second_child_ind]):
                min_child_ind = first_child_ind
            else:
                min_child_ind = second_child_ind
            #switch min child with the parent unless parent is larger
            parent = self.heap[i-1]
            child = self.heap[min_child_ind]
            if(child>=parent):
                break
            else:
                #update values to indices map as an array
                self.indices[child][self.indices[child].index(min_child_ind)] = i-1
                self.indices[parent][self.indices[parent].index(i-1)] = min_child_ind
                self.heap[min_child_ind], self.heap[i-1] = self.heap[i-1], self.heap[min_child_ind]
            i=min_child_ind+1
        return result

    #works in log(n) time due to map keeping track of value indices
    def remove(self, elem):
        if(elem not in self.indices):
            return False
        removal_ind = self.indices[elem][-1]
        self.heap[removal_ind] = -float('inf')
        #remove index from map, and if there are no indices left, remove value
        #key from map
        self.indices[elem].pop()
        if(not self.indices[elem]):
            self.indices.pop(elem)
        #bubble up the -inf value and then remove it!
        i=removal_ind+1
        while(i!=1):
            #update map of values with new parent index as it moves down in the heap
            parent_elem = self.heap[i//2-1]
            self.indices[parent_elem][self.indices[parent_elem].index(i//2-1)] = i-1
            #update element positions in heap array
            self.heap[i-1], self.heap[i//2-1] = self.heap[i//2-1], self.heap[i-1]
            i=i//2

        #now have -inf as the minimum values, so pop it using extract-min operation
        self.popMin()
        #return the element removed
        return elem


#modified to output the shortest path to
#each node given a start node - still needs a connective graph!
#Got O(n*log(n)) time - just needed to add the line to skip adding the edges
#if the min node has already been seen!
def dijkstra_Shortest_Path(start, graph):
    seen = {}
    seen[start] = 0
    #a map of the nodes to the adjacent nodes and the updated cost to that node
    seen_cost_map = {start:[]}

    heapmap = HeapMap()

    next_node = start
    total_path = float("inf")

    #initialize a mapping of costs to nodes for the first node (start)
    cost_map_to_nodes = {}
    for node, cost in graph[start]:
        heapmap.push(cost)
        seen_cost_map[start].append((node, cost))
        if(cost not in cost_map_to_nodes):
            #turn into a deque, not a list!
            cost_map_to_nodes[cost] = [(start, node)]
        else:
            cost_map_to_nodes[cost].append((start, node))

    # print(heapmap.heap)
    seen_len = len(seen)
    graph_len = len(graph)

    #keep adding to seen map until all nodes have been seen
    while(seen_len<graph_len):
        # total_path = float("inf")
        min_cost = heapmap.popMin()

        # print(seen, min_cost)

        #goes through the nodes for this cost until one is found
        #that has not already been seen - and then stops even if
        #some still left for that cost!
        cost_count = 0
        # if(min_cost==25):
        #     print(cost_map_to_nodes[min_cost])
        while(0<len(cost_map_to_nodes[min_cost])):
            #counter for how many to remove from other items if greater than 1
            cost_count+=1
            #gives the last node and this node
            min_node = cost_map_to_nodes[min_cost][0][1]
            curr_node = cost_map_to_nodes[min_cost][0][0]
            # if(min_cost==10):
                # print("Internal count at", cost_count)
            if(min_node in seen and seen[min_node]>min_cost):
                cost_map_to_nodes[min_cost].pop(0)
            else:
                cost_map_to_nodes[min_cost].pop(0)
                for i in range(cost_count-1):
                    heapmap.remove(min_cost)
                break
        else:
            # if(min_cost==10):
                # print("Counted up to", cost_count)
            if(cost_count==1):
                cost_map_to_nodes.pop(min_cost)

                seen_cost_map[curr_node].pop(seen_cost_map[curr_node].index((min_node, min_cost)))
                if(len(seen_cost_map[curr_node])==0):
                    seen_cost_map.pop(curr_node)
            #if more than one value removed, all copies (identical numbers)
            #must be removed from the map
            #NOTE - figure out how to update the other map (seen cost map)
            #later!
            else:
                # print("hello delete")
                for i in range(cost_count):
                    heapmap.remove(min_cost)


        # print(min_node, min_cost, min_node in seen)
        if(min_node in seen):
            continue
        #case where an outgoing edge is found as the minimum cost!
        #iterate through the edges of the new node seen (min_node)
        #and remove internal edges/costs and add new external edges/costs

        for outgoing_node, cost in graph[min_node]:
            #already removed the edge to the current node from the heap!
            if(outgoing_node==curr_node):
                continue
            if outgoing_node in seen:
                #remove all larger paths
                if outgoing_node in seen_cost_map:
                    removals = [a[1] for a in seen_cost_map[outgoing_node] if a[0]==min_node and a[1]>(min_cost+cost)]
                    if(len(removals)>0):
                        for mod_cost in removals:
                            heapmap.remove(mod_cost)

                            if((outgoing_node, min_node) in cost_map_to_nodes[mod_cost]):
                                cost_map_to_nodes[mod_cost].pop(cost_map_to_nodes[mod_cost].index((outgoing_node, min_node)))
                            if(len(cost_map_to_nodes[mod_cost])==0):
                                cost_map_to_nodes.pop(mod_cost)

                            seen_cost_map[outgoing_node].pop(seen_cost_map[outgoing_node].index((min_node, mod_cost)))
                            if(len(seen_cost_map[outgoing_node])==0):
                                seen_cost_map.pop(outgoing_node)
                    #now check for smaller paths
                    # smaller = [a[1] for a in seen_cost_map[outgoing_node] if a[0]==min_node and a[1]<(min_cost+cost)]

                #add new paths that may shortcut to existing "seen" nodes
                #need to add TOTAL path cost here!
                total_cost_to_outgoing_node = min_cost+cost
                if(total_cost_to_outgoing_node<seen[outgoing_node]):
                    heapmap.push(total_cost_to_outgoing_node)
                    # if(min_node==70):
                    #     print(seen_cost_map, total_cost_to_outgoing_node, min_node)
                    if(min_node not in seen_cost_map):
                        seen_cost_map[min_node] = [(outgoing_node, total_cost_to_outgoing_node)]
                    else:
                        seen_cost_map[min_node].append((outgoing_node, total_cost_to_outgoing_node))

                    if(total_cost_to_outgoing_node not in cost_map_to_nodes):
                        cost_map_to_nodes[total_cost_to_outgoing_node] = [(min_node, outgoing_node)]
                    else:
                        cost_map_to_nodes[total_cost_to_outgoing_node].append((min_node, outgoing_node))
            else:
                #need to add TOTAL path cost here!
                total_cost_to_outgoing_node = min_cost+cost
                heapmap.push(total_cost_to_outgoing_node)

                if(min_node not in seen_cost_map):
                    seen_cost_map[min_node] = [(outgoing_node, total_cost_to_outgoing_node)]
                else:
                    seen_cost_map[min_node].append((outgoing_node, total_cost_to_outgoing_node))

                if(total_cost_to_outgoing_node not in cost_map_to_nodes):
                    cost_map_to_nodes[total_cost_to_outgoing_node] = [(min_node, outgoing_node)]
                else:
                    cost_map_to_nodes[total_cost_to_outgoing_node].append((min_node, outgoing_node))

        #set the cost to this node
        if(min_node in seen):
            if(seen[min_node]>min_cost):
                seen[min_node] = min_cost #+seen[curr_node]
        else:
            seen[min_node] = min_cost
            seen_len+=1
        # print(seen[curr_node], seen[min_node], min_node)
    return seen


def bfsConnectivityCheck(s, graph):
    seen = set()
    start = graph[s]
    queue = collections.deque([a[0] for a in start])
    while(queue):
        curr = queue.popleft()
        if(curr not in seen):
            seen.add(curr)
            more_vals = [a[0] for a in graph[curr] if a[0] not in seen]
            queue.extend(more_vals)

    connected_graph = {}
    for node in seen:
        connected_graph[node] = graph[node]

    return connected_graph


# Complete the shortestReach function below.
def shortestReach(n, edges, s):
    graph_map = {}
    #added here for redundancy, but need to add in the read-in phase to get
    #duplicate edges removed before even seen here, or hackerrank will throw
    #a fit! This works on my computer, though
    seen = set()
    for (node1, node2, cost) in edges:
        if((node1, node2, cost) in seen or (node2, node1, cost) in seen):
            continue
        if(node1 in graph_map):
            graph_map[node1].append((node2, cost))
        else:
            graph_map[node1] = [(node2, cost)]

        if(node2 in graph_map):
            graph_map[node2].append((node1, cost))
        else:
            graph_map[node2] = [(node1, cost)]

        seen.add((node1, node2, cost))

    # print(len(graph_map))
    # a = time.clock()
    connected_graph = bfsConnectivityCheck(s, graph_map)
    # for key, values in connected_graph.items():
    #     print("{}:{}".format(key, len(values)))
    # print("Connectivity calc time: ", time.clock()-a)

    shortestPaths = dijkstra_Shortest_Path(s, connected_graph)

    output = []
    for i in range(1, n+1):
        if(s==i):
            continue
        if (i not in connected_graph):
            output.append(-1)
        else:
            output.append(shortestPaths[i])

    return output


if __name__ == '__main__':

    fileHandler = open("input01_dijkstra_BIGBOSS.txt", "r")

    # Get list of all lines in file
    listOfLines = fileHandler.readlines()

    # Close file
    fileHandler.close()

    t = int(listOfLines[0])
    curr_line = 1
    check_arr = []
    for test in range(t):
        input_start = time.clock()
        n, m = map(int, listOfLines[curr_line].split())
        edges = []
        print("There are this many edges: ", m)

        seen = set()

        count_edges_used = 0
        for _ in range(curr_line+1, curr_line+m+1):
            edge = tuple(map(int, listOfLines[_].rstrip().split()))
            if(edge not in seen and (edge[1], edge[0], edge[2]) not in seen):
                count_edges_used+=1
                edges.append(edge)
                seen.add(edge)

        print("There are {} non-duplicate edges".format(count_edges_used))

        print("Time to organize data from input file: {} s".format(time.clock()-input_start))
        curr_line+=m+1
        s = int(listOfLines[curr_line])
        start = time.clock()
        a = shortestReach(n, edges, s)
        print("Dijkstra's running time: {} s".format(time.clock()-start))
        # print(a)
        check_arr.append(a)
        print("test complete - it took {} seconds total".format(time.clock()-input_start))
        curr_line+=1

    fileHandler = open("output07_dijkstra_BIGBOSS.txt", "r")

    # Get list of all lines in file
    listOfLines = fileHandler.readlines()

    # Close file
    fileHandler.close()

    for i in range(t):
        this_ans = check_arr[i]
        actual_ans = list(map(int, listOfLines[i].rstrip().split(" ")))
        print(len(this_ans), len(actual_ans))
        if(this_ans==actual_ans):
            print("TRUE")
        else:
            print("FALSE")
