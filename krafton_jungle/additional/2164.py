from collections import deque
import sys

n = int(sys.stdin.readline())
d = deque()
for i in range(n):
    d.append(i + 1)
while len(d) != 1:
    d.popleft()
    if len(d) == 1:
        break
    d.append(d.popleft())
print(d.pop())