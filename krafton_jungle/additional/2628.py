import sys
a, b = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
l1 = [0, b]
l2 = [0, a]
for _ in range(n):
    t1, t2 = map(int, sys.stdin.readline().split())
    if t1 == 0:
        l1.append(t2)
    else:
        l2.append(t2)

l1.sort()
l2.sort()
l1_max = -1
l2_max = -1
for i in range(1, len(l1)):
    l1_max = max(l1_max, l1[i] - l1[i - 1])
for i in range(1, len(l2)):
    l2_max = max(l2_max, l2[i] - l2[i - 1])
print(l1_max * l2_max)