import sys
n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

s = [[i] for i in range(n)]
maximum = 0
while len(s) > 0:
    t = s.pop()
    #print(s)
    #print(type(t), t)
    if len(t) == n:
        t2 = 0
        for i in range(1, n):
            t2 += abs(l[t[i - 1]] - l[t[i]])
        maximum = max(maximum, t2)
    else:
        for i in range(n):
            if not i in t:
                t3 = t.copy()
                t3.append(i)
                s.append(t3)
print(maximum)