def count_substring(string, sub_string):
    curr_ind = string.find(sub_string)
    if(curr_ind==-1):
        return 0
    else:
        count = 1

    while(curr_ind!=-1):
        curr_ind = string.find(sub_string, curr_ind+1)
        if(curr_ind!=-1):
            count+=1
        else:
            break

    return count

a = input()
b = input()
print(count_substring(a, b))
