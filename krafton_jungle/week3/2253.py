import sys

n, m = map(int, sys.stdin.readline().split())
small = [False for _ in range(n)]
for _ in range(m):
    i = int(sys.stdin.readline())
    small[i - 1] = True

# dp[current_standing][last_jump] = minimum jump
# dp[i][j] = min(dp[i - j][t] | t = j - 1 ~ j + 1)
INIT = sys.maxsize
dp = [[INIT for _ in range(200)] for _ in range(n)]
dp[0][0] = 0

for current_standing in range(n - 1):

    if small[current_standing]:
        continue

    for last_jump in range(200):

        if dp[current_standing][last_jump] >= INIT:
            continue

        for next_jump in range(last_jump - 1, last_jump + 2):
            if not 0 < next_jump < 200:
                continue
        
            next_standing = current_standing + next_jump
            if not next_standing < n:
                break

            dp[next_standing][next_jump] = min(dp[next_standing][next_jump], dp[current_standing][last_jump] + 1)

ans = INIT
for idx in range(200):
    ans = min(ans, dp[n - 1][idx])

if ans == INIT:
    print(-1)
else:
    print(ans)