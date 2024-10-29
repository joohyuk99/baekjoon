from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())

es = list(map(int, sys.stdin.readline().split()))
using_idx = [deque() for _ in range(k + 1)]
using_idx[0].append(0)
for idx, e in enumerate(es):
    using_idx[e].append(idx)
for q in using_idx:
    q.append(k + 1)

multitap = set()
cnt = 0
for e in es:
    using_idx[e].popleft()
    if e in multitap:
        continue
    elif len(multitap) < n:
        multitap.add(e)
    else:
        min_e = 0
        for ue in multitap:
            if using_idx[min_e][0] < using_idx[ue][0]:
                min_e = ue
        multitap.discard(min_e)
        cnt += 1
        multitap.add(e)

print(cnt)