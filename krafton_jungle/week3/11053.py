import sys

n = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))

# dp[last_node] -> maximum length, end in last_node
dp = [1]
for current_idx in range(1, n):
    current_num = seq[current_idx]
    temp = 1
    for compare_idx, compare_length in enumerate(dp):
        compare_num = seq[compare_idx]
        if compare_num < current_num:
            temp = max(temp, compare_length + 1)
    dp.append(temp)

print(max(dp))