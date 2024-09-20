import sys

n, k = map(int, sys.stdin.readline().split())
coin = set()
for _ in range(n):
    t = int(sys.stdin.readline())
    coin.add(t)

dp = [10001 for _ in range(100001)]
dp[0] = 0
for val in coin:
    dp[val] = 1

for i in range(k + 1):
    minimum = dp[i]
    for val in coin:
        if i - val >= 0:
            minimum = min(minimum, dp[i - val] + 1)
    dp[i] = minimum

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])