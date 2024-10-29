import sys

n, k = map(int, sys.stdin.readline().split())
coins = []
for _ in range(n):
    t = int(sys.stdin.readline())
    coins.append(t)

cnt = 0
for val in reversed(coins):
    cnt += k // val
    k = k % val

print(cnt)