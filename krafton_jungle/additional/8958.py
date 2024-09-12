import sys
n = int(sys.stdin.readline())
for _ in range(n):
    t = sys.stdin.readline()
    cnt = 0
    point = 0
    for v in t:
        if v == 'O':
            cnt += 1
            point += cnt
        elif v == 'X':
            cnt = 0
    print(point)