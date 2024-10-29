import sys

n = int(sys.stdin.readline())

l = []

l.append(0)
l.append(1)

for idx in range(2, n + 1):
    l.append(l[idx - 1] + l[idx - 2])

print(l[n])