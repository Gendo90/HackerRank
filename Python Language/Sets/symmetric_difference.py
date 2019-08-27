# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    num_a = int(input())
    a = set(map(int, input().split(" ")))

    num_b = int(input())
    b = set(map(int, input().split(" ")))

    output = [l for l in a.difference(b)]
    output += [k for k in b.difference(a)]
    output = set(output)
    output = list(output)
    output.sort()
    for item in output:
        print(item)
