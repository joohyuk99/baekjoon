import sys

n = int(sys.stdin.readline())

l = []

l.append(0)
l.append(1)
l.append(2)

for idx in range(3, n + 1):
    l.append((l[idx - 1] + l[idx - 2]) % 15746)

print(l[n])