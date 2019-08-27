def count_substring(string, sub_string):
    count = 0
    subs_len = len(sub_string)
    for i in range(len(string)-len(sub_string)+1):
        if(string[i:i+subs_len]==sub_string):
            count+=1

    return count


#counts all substrings with consonants vs. all with vowels
def minion_game_naive(s):
    vowels = {'A':True, 'E':True, 'I':True, 'O':True, 'U':True}
    kevin_seen = {}
    stuart_seen = {}
    stuart_score = 0
    kevin_score = 0

    #first calculate kevin's score by looping through the vowels and then
    #running through the string
    curr_ind = -1
    subs=""
    subs_len = 0
    for vowel in vowels.keys():
        while(curr_ind<len(s)):
            curr_ind = s.find(vowel, curr_ind+1)
            if(curr_ind==-1):
                break
            for i in range(curr_ind+1, len(s)+1):
                subs = s[curr_ind:i]
                if(subs in kevin_seen):
                    continue
                kevin_score+=count_substring(s, subs)
                kevin_seen[subs] = True

    curr_ind = 0
    subs=""
    subs_len = 0
    for i in range(len(s)):
        if(s[i] in vowels):
            continue
        curr_ind = i

        for j in range(curr_ind+1, len(s)+1):
            subs = s[curr_ind:j]
            if(subs in stuart_seen or subs[0] in vowels):
                continue
            stuart_score+=count_substring(s, subs)
            stuart_seen[subs] = True


    if(kevin_score>stuart_score):
        print("Kevin {}".format(kevin_score))
    elif(kevin_score<stuart_score):
        print("Stuart {}".format(stuart_score))
    else:
        print("Draw")

#glanced at the solution and it made sense
#no need to count duplicates of substrings
#just count number of substrings available to each person
#confused by the way they described it - was removing duplicates using a hash
#map before, now just count everything once...
def minion_game(s):
    vowels = {'A':True, 'E':True, 'I':True, 'O':True, 'U':True}
    stuart_score = 0
    kevin_score = 0

    for i, letter in enumerate(s):
        if(letter in vowels):
            kevin_score+=len(s)-i
        else:
            stuart_score+=len(s)-i

    if(kevin_score>stuart_score):
        print("Kevin {}".format(kevin_score))
    elif(kevin_score<stuart_score):
        print("Stuart {}".format(stuart_score))
    else:
        print("Draw")



a = input()
minion_game(a)
