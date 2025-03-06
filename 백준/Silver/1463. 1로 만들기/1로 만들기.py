import sys

n = int(sys.stdin.readline())

l = [0, 0]

for i in range(2, n + 1):
    maxi = l[i - 1] + 1
    if i % 2 == 0 and maxi > l[int(i / 2)] + 1:
        maxi = l[int(i / 2)] + 1
    if i % 3 == 0 and maxi > l[int(i / 3)] + 1:
        maxi = l[int(i / 3)] + 1
    l.append(maxi)

print(l[n])