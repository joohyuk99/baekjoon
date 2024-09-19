import sys
sys.setrecursionlimit(10**8)

n, m = map(int, sys.stdin.readline().split())

vector = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    vector[u - 1].append(v - 1)
    vector[v - 1].append(u - 1)

visited = [-1 for _ in range(n)]
idx = 0
group = 0
while True:
    while idx < n and visited[idx] != -1:
        idx += 1
    if idx == n:
        break
    stack = []
    stack.append(idx)
    visited[idx] = group
    while len(stack) != 0:
        c = stack.pop()
        for arc in vector[c]:
            if visited[arc] == -1:
                visited[arc] = group
                stack.append(arc)
    group += 1
print(group)