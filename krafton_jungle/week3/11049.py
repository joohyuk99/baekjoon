import sys

n = int(sys.stdin.readline())

matrixes = [] # (r, c)
for _ in range(n):
    r, c = map(int, sys.stdin.readline().split())
    matrixes.append((r, c))

# dp[start_index][last_index] = minimum calculate number
# dp[i, j] = min(dp[i, t] + dp[t + 1, j] + i.r * t.c * t.c | t = i ~ j - 1)
dp = [[sys.maxsize for _ in range(n)] for _ in range(n)]
for idx in range(n):
    dp[idx][idx] = 0
for length in range(1, n):
    for start_idx in range(0, n - length):
        last_idx = start_idx + length
        for middle_idx in range(start_idx, last_idx):
            dp[start_idx][last_idx] = min(dp[start_idx][last_idx], 
                                          dp[start_idx][middle_idx] + dp[middle_idx + 1][last_idx] + matrixes[start_idx][0] * matrixes[middle_idx][1] * matrixes[last_idx][1])
            #print(start_idx, middle_idx, last_idx, dp[start_idx][last_idx])

print(dp[0][n - 1])

# for v in dp:
#     print(v)