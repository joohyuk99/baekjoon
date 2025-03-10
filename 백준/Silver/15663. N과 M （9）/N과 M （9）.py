import sys

n, m = map(int, sys.stdin.readline().split())
nl = list(map(int, sys.stdin.readline().split()))
nl.sort()

ans = [0 for _ in range(m)]
ns = set()

def f(cnt):

    # print("cnt: " + str(cnt))
    # print(ans)

    if cnt == m:
        for t in ans:
            print(nl[t], end=" ")
        print()
        return

    i = 0
    while(i < n):
        if i in ns:
            i += 1

        else:
            ans[cnt] = i
            ns.add(i)
            f(cnt + 1)
            ns.remove(i)
            temp = nl[i]
            while(i < n and temp == nl[i]):
                i += 1

f(0)