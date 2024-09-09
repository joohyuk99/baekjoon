import sys

def hwp(n, a, b):
    c = 6 - (a + b)
    if n == 0:
        return 0
    hwp(n - 1, a, c)
    print(a, b)
    hwp(n - 1, c, b)
    
n = int(sys.stdin.readline())
print(2 ** n - 1)
if n <= 20:
    hwp(n, 1, 3)