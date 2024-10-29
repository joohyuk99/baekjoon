import sys

n = int(sys.stdin.readline())
cost = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] # cost[i][j] = i -> j cost

# start, end city index = 0
# dp[travel_bitmask][last_visit] = minimum of remain cost
dp = [[sys.maxsize for _ in range(n)] for _ in range(2 ** n)]
STARTCITY = 0
ENDSTATE = 2 ** n - 1
for last_visit in range(n):
    if cost[last_visit][STARTCITY] != 0:
        dp[ENDSTATE][last_visit] = cost[last_visit][STARTCITY]

for current_state in reversed(range(ENDSTATE + 1)):
    for current_visit in range(n):
        #print("")
        #print("current: ", end="")
        #print(bin(current_state)[2:].zfill(n), current_visit)
        if not current_state & (1 << current_visit): # if current_visit is not visited
            continue

        else:
            current_cost = dp[current_state][current_visit]
            last_state = current_state - (1 << current_visit)
            for last_visit in range(n):
                if not (last_state & (1 << last_visit)) or cost[last_visit][current_visit] == 0:
                    #print(f"skipped: {current_visit}, {last_visit}")
                    continue
                else:
                    dp[last_state][last_visit] = min(dp[last_state][last_visit], current_cost + cost[last_visit][current_visit])
                    #print("update: ", end="")
                    #print(bin(last_state)[2:].zfill(n), last_visit, current_visit, dp[last_state][last_visit])

print(dp[1][0])

# for v in dp:
#     print(v)