import sys
n = int(sys.stdin.readline())
l = []
for _ in range(n):
    t = int(sys.stdin.readline())
    if t == 0: l.pop()
    else: l.append(t)
print(sum(l))