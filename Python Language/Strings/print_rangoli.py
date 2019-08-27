import string
def print_rangoli(size):
    all_letters = [l for l in string.ascii_lowercase]
    letters_used = all_letters[0:size]
    num_lines = 2*size-1
    width = 2*num_lines-1
    curr_letters = [letters_used[size-1]]
    output_rug = []
    for i in range(num_lines):
        back = curr_letters[::-1][:]
        back.pop(0)
        printable_arr = curr_letters[:]+back

        line = ("{:-^"+"{}".format(width)+"s}").format("-".join(printable_arr))
        print(line)
        output_rug.append(line)
        if(i<size-1):
            curr_letters.append(letters_used[size-i-2])
        else:
            curr_letters.pop()

    return output_rug


# a = input()
# k = int(input())

print(print_rangoli(10))
