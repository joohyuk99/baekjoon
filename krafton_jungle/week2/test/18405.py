from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())

board = [[0 for _ in range(n)] for _ in range(n)]
virus = []
for i in range(n):
    buf = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if buf[j] != '0':
            board[i][j] = int(buf[j])
            virus.append((board[i][j], i, j)) # virus, x, y

s, x, y = map(int, sys.stdin.readline().split())

virus.sort()
virus_queue = deque(virus)

DIR = [(-1, 0), (1, 0), (0, 1), (0, -1)]
for _ in range(s):
    #print(board)
    for _ in range(len(virus_queue)):
        temp = virus_queue.popleft()
        current_virus = temp[0]
        current_coord = (temp[1], temp[2])
        for move in DIR:
            next_i, next_j = tuple(t1 + t2 for t1, t2 in zip(move, current_coord))
            if 0 <= next_i < n and 0 <= next_j < n and board[next_i][next_j] == 0:
                board[next_i][next_j] = current_virus
                virus_queue.append((current_virus, next_i, next_j))

print(board[x - 1][y - 1])