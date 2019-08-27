from itertools import permutations
# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    S, r = input().split(" ")
    r = int(r)

    output = ["".join(permuted) for permuted in permutations(S, r)]
    output.sort()
    for ans in output:
        print(ans)
