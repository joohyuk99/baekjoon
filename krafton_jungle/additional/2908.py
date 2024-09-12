import sys
a, b = map(int, sys.stdin.readline().split())

a1 = 0
b1 = 0
for _ in range(3):
    a1 = a1 * 10 + a % 10
    b1 = b1 * 10 + b % 10
    a = a // 10
    b = b // 10
print(max(a1, b1))