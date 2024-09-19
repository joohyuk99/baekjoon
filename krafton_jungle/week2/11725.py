import sys

n = int(sys.stdin.readline())

edge = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    edge[a].append(b)
    edge[b].append(a)

parent = [i for i in range(n + 1)]
stack = [1]
while len(stack) != 0:
    c = stack.pop()
    for val in edge[c]:
        if val != 1 and parent[val] == val:
            parent[val] = c
            stack.append(val)

for i in range(2, n + 1):
    print(parent[i])