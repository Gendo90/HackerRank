def solve(s):
    words = s.split(" ")
    output = [word.capitalize() for word in words]

    return " ".join(output)


# a = input()
# k = int(input())

print(solve("alan herkel 12ac"))
