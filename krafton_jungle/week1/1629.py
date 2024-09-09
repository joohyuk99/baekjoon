import sys
a, b, c = map(int, sys.stdin.readline().split())

def q(n):
    global a, b, c
    if n == 1:
        return a % c
    if n % 2 == 0:
        return (q(n // 2) ** 2) % c
    else:
        return ((q(n // 2) ** 2) * a) % c
    
print(q(b))