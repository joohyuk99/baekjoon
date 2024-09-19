import sys
import heapq

n, m, k, x = map(int, sys.stdin.readline().split())
edge = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    edge[a - 1].append(b - 1)

d = [300001 for _ in range(n)]
d[x - 1] = 0
q = [x - 1]
while len(q) > 0:
    t = heapq.heappop(q)
    #print(t, d)
    for val in edge[t]:
        if d[t] + 1 < d[val]:
            d[val] = d[t] + 1
            heapq.heappush(q, val)

printed = False
for idx, val in enumerate(d):
    if val == k:
        printed = True
        print(idx + 1)

if not printed:
    print(-1)