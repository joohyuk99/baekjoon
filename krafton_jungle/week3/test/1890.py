import sys

n = int(sys.stdin.readline())

board = []
for _ in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    board.append(temp)

# dp[i][j] == number of way
dp = [[0 for _ in range(n)] for _ in  range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            break
        if i + board[i][j] < n:
            dp[i + board[i][j]][j] += dp[i][j]
        if j + board[i][j] < n:
            dp[i][j + board[i][j]] += dp[i][j]
        
        # print(i, j)
        # for v in dp:
        #     print(v)
        # print()

print(dp[n - 1][n - 1])