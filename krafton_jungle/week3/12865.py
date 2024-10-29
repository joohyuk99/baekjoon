import sys

n, k = map(int, sys.stdin.readline().split())

stuffs = []
for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    stuffs.append((w, v))

# dp [stuff_count_index][total_value] = maxumim_total_value
dp = [[0 for _ in range(k + 1)] for _ in range(len(stuffs))]

for stuff_idx, stuff in enumerate(stuffs):
    stuff_weight, stuff_value = stuff
    for total_weight in range(1, k + 1):
        if total_weight < stuff_weight:
            dp[stuff_idx][total_weight] = dp[stuff_idx - 1][total_weight]
        elif stuff_idx == 0 and total_weight == stuff_weight:
            dp[stuff_idx][total_weight] = stuff_value
        elif stuff_idx == 0:
            dp[stuff_idx][total_weight] = dp[stuff_idx][total_weight - 1]
        else:
            dp[stuff_idx][total_weight] = max(dp[stuff_idx - 1][total_weight], dp[stuff_idx][total_weight - 1], dp[stuff_idx - 1][total_weight - stuff_weight] + stuff_value)

print(dp[len(stuffs) - 1][k])

# for v in dp:
#     print(v)