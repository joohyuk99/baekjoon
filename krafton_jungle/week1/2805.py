import sys

n, m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))

l.sort()

s = 0
e = 2000000000
flag = True
mid = 0
while True:
    #print(s, e)
    #input()
    mid = (s + e) // 2 
    su = 0
    for v in l:
        if v > mid:
            su += v - mid

    if m == su or s > e:
        print(mid)
        break
    elif m < su:
        s = mid + 1
    else:
        e = mid - 1