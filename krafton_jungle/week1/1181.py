import sys

l = []
n = int(sys.stdin.readline())
for i in range(n):
    l.append(sys.stdin.readline()[:-1])

l = list(set(l))

l.sort(key = lambda a:(len(a), a))
for t in l:
    print(t)