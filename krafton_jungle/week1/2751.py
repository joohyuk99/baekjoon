import sys

l = []
n = int(sys.stdin.readline())
for i in range(n):
    l.append(int(sys.stdin.readline()))

l.sort()
for t in l:
    print(t)