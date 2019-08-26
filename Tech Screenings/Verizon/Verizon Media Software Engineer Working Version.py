# First technical screening question for Verizon Media Software Engineer
def minOperations(comp_nodes, comp_from, comp_to):
    # Write your code here
    comp_groups = {}
    #could make a map of values back to keys, to see which key it is under...
    #useful later...
    reverse_lookup = {}
    #used for counting the number of computers seen
    comp_seen = {}
    together = zip(comp_from, comp_to)
    if(len(comp_from)+1<comp_nodes):
        return -1

    for link in together:
        comp_seen[link[0]] = True
        comp_seen[link[1]] = True
        if(link[0] in comp_groups):
            comp_groups[link[0]].add(link[1])
            reverse_lookup[link[1]] = link[0]
        elif(link[1] in comp_groups):
            comp_groups[link[1]].add(link[0])
            reverse_lookup[link[0]] = link[1]
        #use reverse lookup here - see if either value is already in a group
        elif(link[1] in reverse_lookup):
            key = reverse_lookup[link[1]]
            if(link[0] not in comp_groups[key]):
                comp_groups[key].add(link[0])
                reverse_lookup[link[0]] = key
                break
        #use reverse lookup here - see if either value is already in a group
        elif(link[0] in reverse_lookup):
            key = reverse_lookup[link[0]]
            if(link[1] not in comp_groups[key]):
                comp_groups[key].add(link[1])
                reverse_lookup[link[1]] = key
                break
        else:
            comp_groups[link[0]] = set()
            comp_groups[link[0]].add(link[1])

        #number of computers in groups of two or more (at least one connection)
        num_comp_groups = len(comp_groups)-1
        #number of computers not connected to anything that need to be connected
        num_computers_disconnect = comp_nodes - len(comp_seen)
        #number of connections that need to be made - each disconnectd computer
        #needs one connection, and there needs to be one connection between
        #computer groups containing multiple computers
        total = num_comp_groups+num_computers_disconnect

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
