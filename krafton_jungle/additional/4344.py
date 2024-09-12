import sys
n = int(sys.stdin.readline())
for _ in range(n):
    t = list(map(int, sys.stdin.readline().split()))
    avg = 0
    for i in range(1, t[0] + 1):
        avg += t[i]
    avg /= t[0]
    cnt = 0
    for i in range(1, t[0] + 1):
        if t[i] > avg:
            cnt += 1
    r = cnt / t[0] * 100
    print(f"{r:.3}%")