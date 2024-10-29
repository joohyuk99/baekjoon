import sys

while True:
    l = list(map(int, sys.stdin.readline().split()))
    if sum(l) == 0:
        sys.exit()
    l.sort()
    if l[0] ** 2 + l[1] ** 2 == l[2] ** 2:
        print("right")
    else:
        print("wrong")