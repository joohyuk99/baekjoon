import sys
n, x = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
for v in l:
    if v < x:
        print(f"{v} ", end="")