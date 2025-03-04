import sys

n, m = map(int, sys.stdin.readline().split())

s = set()
for _ in range(n):
    name = sys.stdin.readline()[:-1]
    s.add(name)

l = []
for _ in range(m):
    name = sys.stdin.readline()[:-1]
    if name in s:
        l.append(name)

l.sort()

print(len(l))
for name in l:
    print(name)