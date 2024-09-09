import sys

l = []
for i in range(9):
    l.append(int(sys.stdin.readline()))

l.sort()
s = sum(l)

n = []
for i in range(9):
    for j in range(i + 1, 9):
            if s - (l[i] + l[j]) == 100:
                n = [l[i], l[j]]

for v in l:
    if not v in n:
        print(v)