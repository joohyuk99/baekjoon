from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
start = [set() for _ in range(n)]
end = [set() for _ in range(n)]
z = set(i for i in range(n))
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    start[a - 1].add(b - 1)
    end[b - 1].add(a - 1)
    z.discard(b - 1)

while len(z) > 0:
    t = z.pop()
    print(t + 1, end=" ")
    for val in start[t]:
        end[val].discard(t)
        if len(end[val]) == 0:
            z.add(val)