import sys
from collections import deque
n = int(input())
q = deque()
for i in range(n):
    t = sys.stdin.readline()
    if t[0:3] == "pus":
        tl = t.split()
        q.append(int(tl[1]))
    elif t[0:3] == "pop":
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif t[0:3] == "siz":
        print(len(q))
    elif t[0:3] == "emp":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif t[0:3] == "fro":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif t[0:3] == "bac":
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])