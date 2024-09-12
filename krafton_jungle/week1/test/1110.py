import sys

# input
n = int(sys.stdin.readline())

# cycle
t = n
idx = 0
while True:
    idx += 1
    t = (t % 10) * 10 + (t // 10 + t % 10) % 10
    
    # if n == t, end cycle
    if n == t:
        break

print(idx)