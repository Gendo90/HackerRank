#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'parliamentParties' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY votes as parameter.
#

def parliamentParties(votes):
    numVotes = len(votes)
    cutOffVoteNum, r = divmod(numVotes, 20)
    if(r>0):
        cutOffVoteNum+=1
    partyMap = {}
    validParties = []

    #populate partyMap
    for vote in votes:
        if(vote in partyMap):
            partyMap[vote]+=1
        else:
            partyMap[vote]=1

    #find validParties
    for party in partyMap.keys():
        if(partyMap[party]>=cutOffVoteNum):
            validParties.append(party)

    validParties.sort()

    return validParties
