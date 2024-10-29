import sys

testcase = int(sys.stdin.readline())
for _ in range(testcase):
    n = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())

    dp = [[0 for _ in range(n)] for _ in range(m + 1)] # dp[money][maximum coin(index)]
    for idx, coin in enumerate(coins):
        for money in range(m + 1):
            #print(money, coin)
            if money < coin:
                continue
            elif money == coin:
                dp[money][idx] = 1
                continue
            else:
                s = 0
                for idx2 in range(idx + 1):
                    s += dp[money - coin][idx2]
                dp[money][idx] = s
            
    
    ans = 0
    for idx in range(n):
        ans += dp[m][idx]
    
    #print(dp)
    print(ans)


# dp(money, maximum coin index)
# dp[i][j] = max(dp[i - coins[j]][t] | t in range(0 ~ j - 1))