import sys

n = -1
max = -1
for i in range(1, 10):
    t = int(sys.stdin.readline())
    if t > max:
        max = t
        n = i

print(max)
print(n)