import sys
n = int(sys.stdin.readline())
if n % 400 == 0: print(1)
elif n % 100 == 0: print(0)
elif n % 4 == 0: print(1)
else: print(0)