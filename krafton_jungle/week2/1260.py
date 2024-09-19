import sys
from collections import deque
n, m, v = map(int, sys.stdin.readline().split())
e = [[False for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    e[a][b] = True
    e[b][a] = True

# DFS
s = [v]
visited = [False for _ in range(n + 1)]
while len(s) != 0:
    c = s.pop()
    if visited[c] == True:
        continue
    else:
        print(f"{c} ", end="")
        visited[c] = True
        for i in range(n, 0, -1):
            if e[c][i] == True and visited[i] == False:
                s.append(i)
print("")

# BFS
q = deque()
q.append(v)
visited = [False for _ in range(n + 1)]
while len(q) != 0:
    c = q.popleft()
    if visited[c] == True:
        continue
    else:
        print(f"{c} ", end="")
        visited[c] = True
        for i in range(1, n + 1):
            if e[c][i] == True and visited[i] == False:
                q.append(i)
print("")