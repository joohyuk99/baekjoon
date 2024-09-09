import sys
a, b = map(int, sys.stdin.readline().split())
q = [i+1 for i in range(a)]
ans = []
idx = -1
while len(ans) < a:
    count = b
    while count:
        idx = (idx + 1) % a
        if q[idx] != -1:
            count -= 1
    ans.append(q[idx])
    q[idx] = -1

print("<", end="")
for idx, v in enumerate(ans):
    if idx == a - 1:
        print(v, end="")
    else:
        print(f"{v}, ", end="")
print(">", end="")