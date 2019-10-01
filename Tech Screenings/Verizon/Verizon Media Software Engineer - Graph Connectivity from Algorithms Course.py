# First technical screening question for Verizon Media Software Engineer

def bfs(start, graph):
    seen = {}
    queue = [start]
    while(queue):
        curr = queue.pop(0)
        for item in graph[curr]:
            if(item not in seen):
                seen[item] = True
                queue.append(item)
    return seen

def minOperations(comp_nodes, comp_from, comp_to):
    # Write your code here
    #hash map containing all nodes encountered thus far
    total_seen = {}
    #graph primitive to hold set of nodes connected to a key node
    graph = {}
    #total count of comp groups
    count = 0
    together = zip(comp_from, comp_to)
    if(len(comp_from)+1<comp_nodes):
        return -1

    #build graph - hash map of nodes, with a set of other nodes the key node
    #links to!
    for edge in together:
        if(edge[0] not in graph):
            graph[edge[0]] = set(edge[1])
        else:
            graph[edge[0]].add(edge[1])
        if(edge[1] not in graph):
            graph[edge[1]] = set(edge[0])
        else:
            graph[edge[1]].add(edge[0])


    for node in range(comp_nodes):
        #case where computer group containing node has not been counted yet
        if(node not in total_seen):
            if(node in graph):
                this_comp_group = bfs(node, graph)
                total_seen.update(this_comp_group)

            else:
                total_seen[node] = True
            count+=1

    #need one less cable than total separate computer groups!
    total = count-1

    #this should be closer and faster, at any rate...
    return total


# Second technical screening question for Verizon Media Software Engineer
def compressWord(word, K):
    # Write your code here
    ind = 0
    while(ind<len(word)-(K-1)):
        if(word[ind:ind+K]==word[ind]*K):
            word = word[:ind] + word[ind+K:]
            if(ind-K>=0):
                ind = ind-K
            else:
                ind = 0
        else:
            ind+=1

    return word


print(compressWord("aabbcccb", 3))
