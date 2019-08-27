# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    a_size = int(input())
    a = set(map(int, input().split(" ")))
    b_size = int(input())
    b = set(map(int, input().split(" ")))

    print(len(a.union(b)))
