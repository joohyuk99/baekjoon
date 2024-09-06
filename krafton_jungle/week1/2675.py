import sys

n = int(sys.stdin.readline())
for a in range(n):
    t = list(sys.stdin.readline().split())
    for v in t[1]:
        for i in range(int(t[0])):
            print(v, end="")
    print()