import sys
import heapq
n = int(sys.stdin.readline())

l = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    l.append((max(a, b), min(a, b)))

d = int(sys.stdin.readline())

for i in range(n):
    cnt = 0
    for j in range(i, n):
        l[i][1]