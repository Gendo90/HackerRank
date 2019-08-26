# First technical screening question for Verizon Media Software Engineer
def minOperations(comp_nodes, comp_from, comp_to):
    # Write your code here
    comp_groups = {}
    #could make a map of values back to keys, to see which key it is under...
    #useful later...
    together = zip(comp_from, comp_to)
    if(len(comp_from)+1<comp_nodes):
        return -1

    for link in together:
        if(link[0] in comp_groups):
            comp_groups[link[0]].add(link[1])
        elif(link[1] in comp_groups):
            comp_groups[link[1]].add(link[0])
        elif(link[1] in comp_groups.values()):
            for key in comp_groups.keys():
                if(link[1] in comp_groups[key] and link[0] not in comp_groups[key]):
                    comp_groups[key].add(link[0])
                    break
        elif(link[0] in comp_groups.values()):
            for key in comp_groups.keys():
                if(link[0] in comp_groups[key] and link[1] not in comp_groups[key]):
                    comp_groups[key].add(link[1])
                    break
        else:
            comp_groups[link[0]] = set()
            comp_groups[link[0]].add(link[1])

    #need to include the computers not connected to anything
    #currently off by a factor of comp_nodes-len(comp_seen) where
    #comp_seen is given as a map of the computer values encountered in together
    return len(comp_groups)-1


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
