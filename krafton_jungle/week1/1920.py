import sys

n1 = input()
l1 = list(map(int, sys.stdin.readline().split()))
n2 = input()
l2 = list(map(int, sys.stdin.readline().split()))

d = {}
for v in l1:
    d[v] = True

for v in l2:
    if v in d:
        print(1)
    else:
        print(0)