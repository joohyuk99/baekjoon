import sys

n = int(sys.stdin.readline())

if n == 1:
    sys.exit(0)

else:
    for i in range(2, n + 1):
        while(n % i == 0):
            print(i)
            n = n / i