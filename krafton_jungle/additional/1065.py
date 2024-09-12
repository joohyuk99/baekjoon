import sys
n = int(sys.stdin.readline())
cnt = 0
for i in range(n):
    t = i + 1
    if t < 100:
        cnt += 1
    else:
        if t % 10 - t // 10 % 10 == t // 10 % 10 - t // 100:
            cnt += 1
print(cnt)