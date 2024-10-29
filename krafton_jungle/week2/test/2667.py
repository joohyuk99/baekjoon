import sys

VISITED = -1
DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]

n = int(sys.stdin.readline())

apt = [[None for _ in range(n)] for _ in range(n)]
for i in range(n):
    buf = sys.stdin.readline()
    for j in range(n):
        apt[i][j] = int(buf[j])

ans = []
for i in range(n):
    for j in range(n):

        if apt[i][j] == VISITED:
            continue

        elif apt[i][j] == 1:
            #print(i, j, apt)
            apt[i][j] = VISITED

            stack = []
            cnt = 0
            stack.append((i, j))
            while stack:
                current_coord = stack.pop()
                cnt += 1
                for move in DIR:
                    next_i, next_j = tuple(t1 + t2 for t1, t2 in zip(move, current_coord))
                    #print("next", next_i, next_j, stack)
                    if not 0 <= next_i < n or not 0 <= next_j < n or not apt[next_i][next_j] == 1:
                        continue

                    apt[next_i][next_j] = VISITED
                    stack.append((next_i, next_j))
            ans.append(cnt)

ans.sort()
print(len(ans))
for val in ans:
    print(val)