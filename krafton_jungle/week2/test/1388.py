import sys

n, m = map(int, sys.stdin.readline().split())

board = []
for _ in range(n):
    board.append(sys.stdin.readline())

visited = [[False for _ in range(m)] for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(m):
        
        if visited[i][j]:
            continue
        
        visited[i][j] = True
        if board[i][j] == '-':
            cnt += 1
            next_j = j
            while next_j > 0:
                next_j -= 1
                if visited[i][next_j] or board[i][next_j] != '-':
                    break
                else: 
                    visited[i][next_j] = True
            
            next_j = j
            while next_j < m - 1:
                next_j += 1
                if visited[i][next_j] or board[i][next_j] != '-':
                    break
                else:
                    visited[i][next_j] = True
        
        elif board[i][j] == '|':
            cnt += 1
            next_i = i
            while next_i > 0:
                next_i -= 1
                if visited[next_i][j] or board[next_i][j] != '|':
                    break
                else: 
                    visited[next_i][j] = True
            
            next_i = i
            while next_i < n - 1:
                next_i += 1
                if visited[next_i][j] or board[next_i][j] != '|':
                    break
                else:
                    visited[next_i][j] = True
        #print(i, j, cnt)

print(cnt)