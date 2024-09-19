import sys
sys.setrecursionlimit(10**8)
v, e = map(int, sys.stdin.readline().split())
edge = []
for _ in range(e):
    a, b, d = map(int, sys.stdin.readline().split())
    edge.append((d, a - 1, b - 1)) # weight, start_point, end_point
edge.sort()
r = [i for i in range(v)]
def root(n):
    if r[n] == n:
        return n
    else:
        return root(r[n])
def union(a, b):
    ra = root(a)
    rb = root(b)
    if ra == rb:
        return -1
    elif ra < rb:
        r[rb] = r[ra]
        r[b] = r[ra]
    elif rb < ra:
        r[ra] = r[rb]
        r[a] = r[rb]
s = 0
cnt = 0
for val in edge:
    if cnt == v - 1:
        break
    else:
        if union(val[1], val[2]) != -1:
            s += val[0]
            cnt += 1
print(s)