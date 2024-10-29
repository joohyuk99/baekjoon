import sys

n = int(sys.stdin.readline())
stair = [0]
for _ in range(n):
    temp = int(sys.stdin.readline())
    stair.append(temp)

# dp[stair][+1 num]
dp = [[sys.maxsize * -1 for _ in range(2)] for _ in range(n + 1)]
dp[0][0] = 0
dp[1][0] = stair[1]
for current_stair in range(2, n + 1):
    
    # last jump is 1
    dp[current_stair][1] = max(dp[current_stair][1], dp[current_stair - 1][0] + stair[current_stair])

    # last jump is 2 or 3
    if 0 <= current_stair - 2:
        dp[current_stair][0] = max(dp[current_stair - 2][0], dp[current_stair - 2][1]) + stair[current_stair]
    
#print(dp)
print(max(dp[n][0], dp[n][1]))