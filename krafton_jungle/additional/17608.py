import sys
n = int(sys.stdin.readline())
l = []
for _ in range(n):
    t = int(sys.stdin.readline())
    l.append(t)

cnt = 0
maxi = 0
for i in range(n - 1, -1, -1):
    if l[i] > maxi:
        maxi = l[i]
        cnt += 1
print(cnt)