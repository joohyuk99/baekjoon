import sys
import heapq

n = int(sys.stdin.readline())

q = []
cnt = 0
for _ in range(n):
    t = int(sys.stdin.readline())
    heapq.heappush(q, t)
while len(q) > 1:
    t1 = heapq.heappop(q)
    t2 = heapq.heappop(q)
    cnt += t1
    cnt += t2
    heapq.heappush(q, (t1 + t2))
print(cnt)