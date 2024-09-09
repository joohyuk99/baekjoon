import sys
sys.setrecursionlimit(10**8)

global n
n = int(sys.stdin.readline())
cost = []
for i in range(n):
    cost.append(list(map(int, sys.stdin.readline().split())))

start_point = 0
end_state = (2 ** n) - 1
dp = [[10000000 for i in range(n)] for j in range(2 ** n)] # dp[state][last_visit]

for i in range(n):
    if cost[i][start_point]:
        dp[end_state][i] = cost[i][start_point]

for current_state in range(2 ** n - 2, -1, -1):
    for last_visit in range(n):
        if current_state & (1 << last_visit):
            for next_visit in range(n):
                if (not (current_state & (1 << next_visit))) and cost[last_visit][next_visit]:
                    dp[current_state][last_visit] = min(dp[current_state][last_visit], dp[current_state | (1 << next_visit)][next_visit] + cost[last_visit][next_visit])

print(dp[1][0])