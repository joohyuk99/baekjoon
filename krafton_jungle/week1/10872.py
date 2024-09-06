import sys
def f(n):
    if n == 0:
        return 1
    return n * f(n - 1)
n = int(sys.stdin.readline())
print(f(n))