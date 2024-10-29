import sys

string1 = sys.stdin.readline()[:-1]
string2 = sys.stdin.readline()[:-1]

# def printM():
#     for m in dp:
#         print(m)

dp = [[0 for _ in range(len(string2))] for _ in range(len(string1))]

if string1[0] == string2[0]:
    dp[0][0] = 1

for idx in range(1, len(string1)):
    if string1[idx] == string2[0]:
        dp[idx][0] = max(dp[idx - 1][0], 1)
    else:
        dp[idx][0] = dp[idx - 1][0]

for idx in range(1, len(string2)):
    if string1[0] == string2[idx]:
        dp[0][idx] = max(dp[0][idx - 1], 1)
    else:
        dp[0][idx] = dp[0][idx - 1]


for i in range(1, len(string1)):
    for j in range(1, len(string2)):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        if string1[i] == string2[j]:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
        #print(i, j, string1[i], string2[j])

# printM()
print(dp[len(string1) - 1][len(string2) - 1])

# dp(i, j)
# 1) if s1[i] != s2[j] -> max(dp(i, j - 1), dp(i - 1, j))
# 2) if s1[i] == s2[j] -> max(dp(i, j - 1), dp(i - 1, j), dp(i - 1, j - 1) + 1)