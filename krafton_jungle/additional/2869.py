import sys
a, b, v = map(int, sys.stdin.readline().split())
t = a - b
v -= a
q = v // t
if t * q == v: print(q + 1)
else: print(q + 2)