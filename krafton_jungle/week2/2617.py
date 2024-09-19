import sys

n, m = map(int, sys.stdin.readline().split())

h = {}
l = {}
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if not a - 1 in h:
        h[a - 1] = []
    h[a - 1].append(b - 1)
    if not b - 1 in l:
        l[b - 1] = []
    l[b - 1].append(a - 1)
#print(h, l)
dp_h = [-1 for _ in range(n)]
def ch(c):
    visited[c] = True
    #if dp_h[c] != -1:
    #    return dp_h[c]
    if not c in h:
        dp_h[c] = 0
        return 0
    else:
        s = 0
        for val in h[c]:
            if not visited[val]:
                s += 1
                s += ch(val)
        dp_h[c] = s
        return s

dp_l = [-1 for _ in range(n)]
def cl(c):
    #print(c, visited)
    visited[c] = True
    #if dp_l[c] != -1:
    #    return dp_l[c]
    if not c in l:
        dp_l[c] = 0
        return 0
    else:
        s = 0
        for val in l[c]:
            if not visited[val]:
                s += 1
                s += cl(val)
        dp_l[c] = s
        return s
    
cnt = 0
for i in range(n):
    visited = [False for _ in range(n)]
    if ch(i) > n // 2:
        cnt += 1
    visited = [False for _ in range(n)]
    if cl(i) > n // 2:
        cnt += 1
    #print(dp_h, dp_l)
print(cnt)