from collections import deque
import sys

# input
m, n, h = map(int, sys.stdin.readline().split())
rapedTomato = []
dp = [[[1000001 for _ in range(m)] for _ in range(n)] for _ in range(h)]
for h_idx in range(h):
    for n_idx in range(n):
        temp = list(map(int, sys.stdin.readline().split()))
        for m_idx in range(len(temp)):
            if temp[m_idx] == 1:
                dp[h_idx][n_idx][m_idx] = 0
                rapedTomato.append((h_idx, n_idx, m_idx))
            elif temp[m_idx] == -1:
                dp[h_idx][n_idx][m_idx] = 0


MOVE = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

# search shortest path
q = deque()
for startTomato in rapedTomato:
    h_idx, n_idx, m_idx = startTomato
    q.append(((h_idx, n_idx, m_idx), 0)) # current location, day

while len(q) > 0:
    current_location, current_day = q.popleft()
    if dp[current_location[0]][current_location[1]][current_location[2]] < current_day:
        continue

    for move_idx in MOVE:
        next_idx = tuple(i + j for i, j in zip(current_location, move_idx))

        # check next location is valid
        indexingError = True
        # for dir in next_idx:
        #     if dir < 0:
        #         indexingError = True
        # if next_idx[0] == h or next_idx[1] == n or next_idx[2] == m:
        #     indexingError = True
        if move_idx == (1, 0, 0):
            if current_location[0] < h - 1:
                indexingError = False
        elif move_idx == (-1, 0, 0):
            if current_location[0] > 0:
                indexingError = False
        elif move_idx == (0, 1, 0):
            if current_location[1] < n - 1:
                indexingError = False
        elif move_idx == (0, -1, 0):
            if current_location[1] > 0:
                indexingError = False
        elif move_idx == (0, 0, 1):
            if current_location[2] < m - 1:
                indexingError = False
        elif move_idx == (0, 0, -1):
            if current_location[2] > 0:
                indexingError = False
        
        if not indexingError:
            next_location = dp[next_idx[0]][next_idx[1]][next_idx[2]]
            #print(next_location, current_day)
            if 0 < next_location and current_day + 1 < next_location:
                dp[next_idx[0]][next_idx[1]][next_idx[2]] = current_day + 1
                q.append((next_idx, current_day + 1))
                #print(next_idx, current_day, q)

maximum = 0
for h_idx in range(h):
    for n_idx in range(n):
        for m_idx in range(m):
            maximum = max(maximum, dp[h_idx][n_idx][m_idx])

if maximum == 1000001:
    print(-1)
else:
    print(maximum)