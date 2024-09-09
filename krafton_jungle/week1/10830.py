import sys
sys.setrecursionlimit(10**6)
a, b = map(int, sys.stdin.readline().split())

l = []

for i in range(a):
    l.append(list(map(int, sys.stdin.readline().split())))

m = {}

dp = {}

def mult(m1, m2):
    global a
    ret1 = [[0 for _ in range(a)] for _ in range(a)]
    for i in range(a):
        for j in range(a):
            for k in range(a):
                ret1[i][j] += m1[i][k] * m2[k][j]
                #ret[i][j] += m1[k][j] + m2[i][k]
            ret1[i][j] = ret1[i][j] % 1000

    return ret1

def q(we):
    n = we
    #print(f" {n}")
    global a
    if n == 0:
        return dp[0]
    else:
        ret2 = [[0 for _ in range(a)] for _ in range(a)]
        tt = []
        idx = 0
        while n > 0:
            if n % 2 == 1:
                tt.append(idx)
            idx += 1
            n = n // 2
        #print(we, tt)
        if len(tt) == 1:
            if tt[0] in dp:
                return dp[tt[0]]
            else:
                dp[tt[0]] = mult(q((1 << tt[0]) // 2), q((1 << tt[0]) // 2))
                #print("dp[tt[0]]: ", dp[tt[0]], we)
                return dp[tt[0]]
        else:
            ret2 = q(1 << tt[0])
            for k in range(1, len(tt)):
                ret2 = mult(ret2, q(1 << tt[k]))
                #print("ret: ", ret2, we)
            return ret2


dp[0] = l
l = q(b)
for i in range(a):
    for j in range(a):
        print(f"{l[i][j] % 1000} ", end="")
    print("")