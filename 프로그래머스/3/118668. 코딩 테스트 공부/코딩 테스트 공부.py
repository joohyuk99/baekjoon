import math

def solution(alp, cop, problems):
    
    g_a, g_c = 0, 0
    for p in problems:
        req_a, req_c, _, _, _ = p
        if g_a < req_a:
            g_a = req_a
        if g_c < req_c:
            g_c = req_c
            
    dp = [[math.inf for _ in range(g_c + 1)] for _ in range(g_a + 1)]
    
    alp = min(g_a, alp)
    cop = min(g_c, cop)
    dp[alp][cop] = 0
    
    for a in range(alp, g_a + 1):
        for c in range(cop, g_c + 1):
            if a < g_a and dp[a + 1][c] > dp[a][c] + 1:
                dp[a + 1][c] = dp[a][c] + 1
            if c < g_c and dp[a][c + 1] > dp[a][c] + 1:
                dp[a][c + 1] = dp[a][c] + 1
            for p in problems:
                req_a, req_c, rwd_a, rwd_c, cost = p
                if a >= req_a and c >= req_c:
                    na, nc = a + rwd_a, c + rwd_c
                    if na > g_a:
                        na = g_a
                    if nc > g_c:
                        nc = g_c
                    if dp[na][nc] > dp[a][c] + cost:
                        dp[na][nc] = dp[a][c] + cost
                    
    return dp[g_a][g_c]