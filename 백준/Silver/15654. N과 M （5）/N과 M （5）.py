import sys

n, m = map(int, sys.stdin.readline().split())
nl = list(map(int, sys.stdin.readline().split()))
nl.sort()

ans = [0 for _ in range(m)]
ns = set()

def f(cnt, lidx):

    if cnt == m:
        for t in ans:
            print(nl[t], end=" ")
        print()
        return
    
    for i in range(n):
        if i not in ns:
            ans[cnt] = i
            ns.add(i)
            f(cnt + 1, i)
            ns.remove(i)
    
f(0, -1)