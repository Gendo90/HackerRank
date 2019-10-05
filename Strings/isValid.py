#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    letters = {}
    isValid = "YES"
    for letter in s:
        if(letters.get(letter)):
            letters[letter] +=1
        else:
            letters[letter] = 1
    # print(letters)
    vals = [a for a in letters.values()]
    test_freq = vals[0]
    i=1
    while(i<len(vals) and test_freq==vals[i]):
        i+=1
    if(i==len(vals)):
        return isValid
    else:
        if((not ((test_freq==1 or vals[i]==1) and len(vals)>3) ) and (vals[i]+1<test_freq or test_freq+1<vals[i])):
            return "NO"
        else:
            a = vals.pop(i)
            if(all(v==test_freq for v in vals)):
                return isValid
            vals.append(a)
            vals.pop(0)
            if(all(v==a for v in vals)):
                return isValid
    return "NO"


print(isValid("abcdefghhgfedecba"))
print(isValid("aabbcd"))
print(isValid("ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd"))
print(isValid("aaaaaabc"))
