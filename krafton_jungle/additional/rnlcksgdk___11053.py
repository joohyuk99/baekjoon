import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline()))
dp = [[0 for _ in range(n)] for _ in range(n)] # [start_index][end_index]
m = [[(0, 0) for _ in range(n)] for _ in range(n)]

for i in range(n):
    dp[i][i] = 1
    m[i][i] = l[i]

for i in range(1, n): # start index
    for j in range(i, n): # last index
        if m[i][j - 1] < l[j]:
            m[i][j] = l[j]
            dp[i][j] = dp[i][j - 1] + 1
        else:
            m[i][j] = m[i][j - 1]
            dp[i][j] = dp[i][j - 1]
        for k in range(j + 1, i):
            if l[k] > l[j]