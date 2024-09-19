from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
maze = [[] for _ in range(n)]
for i in range(n):
    t = sys.stdin.readline()
    for j in range(len(t) - 1):
        maze[i].append(int(t[j]))
#print(maze)

s = [[0 for _ in range(m)] for _ in range(n)]
q = deque()
q.append((0, 0)) # i, j, cost
s[0][0] = 1
while len(q) > 0:
    i, j = q.popleft()
    if i > 0 and maze[i - 1][j] == 1 and s[i - 1][j] == 0:
        s[i - 1][j] = s[i][j] + 1
        q.append((i - 1, j))
    if i < n - 1 and maze[i + 1][j] == 1 and s[i + 1][j] == 0:
        s[i + 1][j] = s[i][j] + 1
        q.append((i + 1, j))
    if j > 0 and maze[i][j - 1] == 1 and s[i][j - 1] == 0:
        s[i][j - 1] = s[i][j] + 1
        q.append((i, j - 1))
    if j < m - 1 and maze[i][j + 1] == 1 and s[i][j + 1] == 0:
        s[i][j + 1] = s[i][j] + 1
        q.append((i, j + 1))

print(s[n - 1][m - 1])