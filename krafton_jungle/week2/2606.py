import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

edge = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)

cnt = -1
visited = [False for _ in range(n)]
stack = [0]
visited[0] = True
while len(stack) != 0:
    #print(stack)
    c = stack.pop()
    cnt += 1
    for val in edge[c]:
        if not visited[val]:
            stack.append(val)
            visited[val] = True

print(cnt)