import sys
n = int(sys.stdin.readline())
l = [0 for _ in range(10001)]
for _ in range(n):
    t = int(sys.stdin.readline())
    l[t] += 1

for i, v in enumerate(l):
    for _ in range(v):
        print(i)