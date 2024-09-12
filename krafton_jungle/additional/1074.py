import sys
n, r, c = map(int, sys.stdin.readline().split())
def f(n1, r1, c1):
    if n1 == 0:
        return 0
    else:
        t1 = r1 // (2 ** (n1 - 1))
        t2 = c1 // (2 ** (n1 - 1))
        if t1 == 0 and t2 == 0:
            return f(n1 - 1, r1, c1)
        elif t1 == 1 and t2 == 0:
            return (2 ** (n1 - 1)) ** 2 + f(n1 - 1, r1 - (2 ** (n1 - 1)), c1)
        elif t1 == 0 and t2 == 1:
            return ((2 ** (n1 - 1)) ** 2) * 2 + f(n1 - 1, r1, c1 - (2 ** (n1 - 1)))
        else:
            return ((2 ** (n1 - 1)) ** 2) * 3 + f(n1 - 1, r1 - (2 ** (n1 - 1)), c1 - (2 ** (n1 - 1)))
print(f(n, c, r))