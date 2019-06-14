def timeConversion(s):
    #
    # Write your code here.
    #
    h = (s[0:2])
    m = (s[3:5])
    sec = (s[6:8])
    if("P" in s):
        if(int(h)!=12):
            h=str((int(h)+12))
    else:
        if(int(h)==12):
            h="00"

    output = h+":"+m+":"+sec
    return output

print(timeConversion("07:05:45AM"))
