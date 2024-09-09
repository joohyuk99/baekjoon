import sys
import heapq
n = int(sys.stdin.readline())

l = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    l.append((min(a, b), max(a, b)))

d = int(sys.stdin.readline())

