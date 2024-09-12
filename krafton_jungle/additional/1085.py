import sys
x, y, w, h = map(int, sys.stdin.readline().split())
w -= x
h -= y
print(min(min(x, y), min(w, h)))