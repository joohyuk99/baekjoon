import sys
n = []
for _ in range(3):
    n.append(int(sys.stdin.readline()))
t = 1
for v in n:
    t *= v
mp = [0 for _ in range(10)]
while t > 0:
    mp[t % 10] += 1
    t = t // 10
for v in mp:
    print(v)