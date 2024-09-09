import sys
def q(n, end):
    if n == end:
        return 1
    cnt = 0
    if n == 0:
        for i in range(end):
            m.append([i, 0])
            cnt += q(n + 1, end)
            m.pop()
    else:
        for i in range(end):

#            print(i, n, m)
#            d = [['_' for i in range(end)] for j in range(end)]
#            for a_i, t in enumerate(m):
#                d[t[0]][t[1]] = 'O'
#            d[i][n] = 'O'
#            for a_a in d:
#                print(a_a)
#            print()

            flag = True
            for v in m:
                if i + n == v[0] + v[1] or i - n == v[0] - v[1] or i == v[0]:
                    flag = False
            if flag:
                m.append([i, n])
                cnt += q(n + 1, end)
                m.pop()
    return cnt

n = int(sys.stdin.readline())
m = []
print(q(0, n))