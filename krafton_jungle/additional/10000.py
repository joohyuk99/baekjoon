import sys
n = int(sys.stdin.readline())

l = []
for i in range(n):
    a, b = map(int, sys.stdin.readline())
    l.append(a - b, i)
    l.append(a + b, i)

c = {}
cnt = 0
s = []
for v in l:
    if 