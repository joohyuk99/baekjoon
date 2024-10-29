from collections import deque
import sys
str = sys.stdin.readline()[:-1]
l = [0 for _ in range(ord('A'), ord('Z') + 1)]
for s in str:
    l[ord(s) - ord('A')] += 1
ans = deque()
for idx, c in enumerate(l):
    if c % 2 == 1:
        if ans:
            print("I'm Sorry Hansoo")
            sys.exit()
        else:
            ans.append(chr(idx + ord('A')))
            l[idx] -= 1
            
for i, c in enumerate(reversed(l)):
    idx = len(l) - i - 1
    while l[idx] > 0:
        ans.appendleft(chr(idx + ord('A')))
        ans.append(chr(idx + ord('A')))
        l[idx] -= 2

for v in ans:
    print(v, end="")
print("")