from collections import deque
import sys
import heapq

n = int(sys.stdin.readline())
start_set = set(i for i in range(n))
edge = [set() for _ in range(n)]
indegree = [0 for _ in range(n)]
for i in range(n):
    buf = sys.stdin.readline()
    for j in range(n):
        if buf[j] == '1':
            edge[i].add(j)
            indegree[j] += 1