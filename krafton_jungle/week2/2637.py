from collections import deque
import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

low_to_high = [{} for _ in range(n)]
high_to_low = [set() for _ in range(n)]

basic_parts = set(i for i in range(n))

for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    low_to_high[y - 1][x - 1] = z
    high_to_low[x - 1].add(y - 1)
    basic_parts.discard(x - 1)

q = deque()
parts = [{} for _ in range(n)] # need dp[i][j] * j for make i
for basic_part in basic_parts:
    q.append(basic_part)
    parts[basic_part][basic_part] = 1

while len(q) > 0:
    current_part = q.popleft()
    for parent_part, num in low_to_high[current_part].items():
        high_to_low[parent_part].discard(current_part)
        for child_parts, parts_num in parts[current_part].items():
            if not child_parts in parts[parent_part]:
                parts[parent_part][child_parts] = 0
            parts[parent_part][child_parts] += num * parts_num
        if len(high_to_low[parent_part]) == 0:
            q.append(parent_part)

h = []
for key, val in parts[n - 1].items():
    heapq.heappush(h, (key, val))

while len(h) > 0:
    idx, num = heapq.heappop(h)
    print(f"{idx + 1} {num}")