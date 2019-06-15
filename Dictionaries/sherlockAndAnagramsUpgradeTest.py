#!/bin/python3

import math
import os
import random
import re
import sys
import time

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    seen_substrings = {}
    #length of the substring, up to len(s)-2
    i=1

    #test for case where all letters are the same!
    first_letter = s[0]
    testCase = []
    for letter in s:
        if(letter==first_letter):
            testCase.append(True)
        else:
            testCase.append(False)

    if(all(testCase)):
        total=0
        counter=[0]
        itera = len(s)
        while(itera!=1):
            counter.append(counter[-1]+1)
            total+=sum(counter)
            itera-=1
        return total
    # currently iterates over the possible substrings correctly
    # need to make it able to compare substrings to see if they have the
    # same letters
    while(i<len(s)):
        for ind, subst in enumerate(s):
            if(ind+i>len(s)):
                break
            # substring to compare to other substrings in s
            this_subs = s[ind:ind+i]
            # print(this_subs)
            for segment in range(ind+1, len(s)):
                compared_subs = s[segment:segment+i]
                if(len(compared_subs)!=len(this_subs)):
                    break
                # print(this_subs, compared_subs)
                # ~5 seconds better already! need to optimize more than just shifting the
                # continue here
                validCase = True
                for n in this_subs:
                    if(compared_subs.count(n)!=this_subs.count(n)):
                        validCase = False
                        break
                if(not validCase):
                    continue
                # print(this_subs, compared_subs)
                if(all(True if x in compared_subs else False for x in this_subs) and all(True if x in this_subs else False for x in compared_subs)):
                # print(this_subs, compared_subs)

                # print(this_subs, compared_subs)
                    if(this_subs not in seen_substrings):
                        seen_substrings[this_subs]=1
                    else:
                        seen_substrings[this_subs]+=1
        i+=1
    # print(seen_substrings)
    return sum(seen_substrings[a] for a in seen_substrings.keys())

a = time.clock()
print(sherlockAndAnagrams("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(sherlockAndAnagrams("bbcaadacaacbdddcdbddaddabcccdaaadcadcbddadababdaaabcccdcdaacadcababbabbdbacabbdcbbbbbddacdbbcdddbaaa"))
print(sherlockAndAnagrams("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(sherlockAndAnagrams("cacccbbcaaccbaacbbbcaaaababcacbbababbaacabccccaaaacbcababcbaaaaaacbacbccabcabbaaacabccbabccabbabcbba"))
print(sherlockAndAnagrams("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(sherlockAndAnagrams("bbcbacaabacacaaacbbcaabccacbaaaabbcaaaaaaaccaccabcacabbbbabbbbacaaccbabbccccaacccccabcabaacaabbcbaca"))
print(sherlockAndAnagrams("cbaacdbaadbabbdbbaabddbdabbbccbdaccdbbdacdcabdbacbcadbbbbacbdabddcaccbbacbcadcdcabaabdbaacdccbbabbbc"))
print(sherlockAndAnagrams("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(sherlockAndAnagrams("babacaccaaabaaaaaaaccaaaccaaccabcbbbabccbbabababccaabcccacccaaabaccbccccbaacbcaacbcaaaaaaabacbcbbbcc"))
print(sherlockAndAnagrams("bcbabbaccacbacaacbbaccbcbccbaaaabbbcaccaacaccbabcbabccacbaabbaaaabbbcbbbbbaababacacbcaabbcbcbcabbaba"))
b = time.clock()
print(b-a)
