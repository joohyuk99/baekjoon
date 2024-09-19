import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
bus = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    bus[a - 1].append((c, b - 1))
start, end = map(int, sys.stdin.readline().split())