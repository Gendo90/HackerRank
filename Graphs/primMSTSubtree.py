#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np
import time

import heapq
import sys


#Enhanced heap data structure that uses a map to store value indices and
#remove elements in O(log(n)) time - as compared to O(n) removal time for
#regular heaps, including python's builtin heapq package

#Example uses are Dijkstra's upgraded algorithm, Prim's upgraded MST algorithm

#only works for distinct values right now!
#TODO: extend for multiple identical values by using arrays in the self.indices map
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


#assumes graph is connected
def primMST_upgraded(n, edges, start):
    #build graph
    graph = {}
    for i in range(1, n+1):
        graph[i]=set()

    for edge in edges:
        graph[edge[0]].add((edge[1], edge[2]))
        graph[edge[1]].add((edge[0], edge[2]))

    MST = {start:set()}
    heapmap = HeapMap()
    # print("heap is ", heapmap.heap)
    cost_map_to_nodes = {}
    for node_to, cost in graph[start]:
        # print(cost)
        heapmap.push(cost)
        if(cost not in cost_map_to_nodes):
            cost_map_to_nodes[cost] = [(start, node_to)]
        else:
            cost_map_to_nodes[cost].append((start, node_to))

    #rewrite loop below to only add costs to heap if nodes_to are not in the
    #MST and to remove costs from the heap if nodes_to are already in the
    #MST for each new node added based on the cost
    while(len(MST)<n):
        #dummy values for minimum edge cost and minimum edge and edge connected
        #to the edge being brought into the MST
        min_cost = heapmap.popMin()

        while(0<len(cost_map_to_nodes[min_cost])):
            min_node = cost_map_to_nodes[min_cost][0][1]
            curr_node = cost_map_to_nodes[min_cost][0][0]
            if(min_node in MST):
                cost_map_to_nodes[min_cost].pop(0)
            else:
                break
        else:
            cost_map_to_nodes.pop(min_cost)

        #skips redundant values
        if(curr_node in MST and min_node in MST):
            continue

        #case where an outgoing edge is found as the minimum cost!
        #iterate through the edges of the new node added to the MST (min_node)
        #and remove internal edges/costs and add new external edges/costs
        for outgoing_node, cost in graph[min_node]:
            #already removed the edge to the current node from the heap!
            if(outgoing_node==curr_node):
                continue
            if outgoing_node in MST:
                heapmap.remove(cost)
                cost_map_to_nodes[cost].pop(cost_map_to_nodes[cost].index((outgoing_node, min_node)))
                if(len(cost_map_to_nodes[cost])==0):
                    cost_map_to_nodes.pop(cost)
            else:
                heapmap.push(cost)
                if(cost not in cost_map_to_nodes):
                    cost_map_to_nodes[cost] = [(min_node, outgoing_node)]
                else:
                    cost_map_to_nodes[cost].append((min_node, outgoing_node))

        #add min_node that was not in the MST to the MST
        MST[min_node] = set()
        #add new edges and costs to the MST, for the node in the MST already
        #and the new node added to the MST
        MST[min_node].add((curr_node, min_cost))
        MST[curr_node].add((min_node, min_cost))

    return calcMSTSum(MST)

def calcMSTSum(MST):
    total = 0
    queue = [1]
    seen = {}
    while(queue):
        curr = queue.pop(0)
        if(curr not in seen):
            more_nodes = [a[0] for a in MST[curr] if a[0] not in seen]
            queue.extend(more_nodes)
            total+=sum(a[1] for a in MST[curr] if a[0] not in seen)
            seen[curr] = True
    return total

if __name__ == '__main__':
    n = 4
    edges = [[2, 1, 1000], [3, 4, 299], [2, 4, 200], [2, 4, 100], [3, 2, 300], [3, 2, 6]]

    print(primMST_upgraded(n, edges, 2))
