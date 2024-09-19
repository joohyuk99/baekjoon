import sys

n, m = map(int, sys.stdin.readline().split())
ice = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ice2 = [[0 for _ in range(m)] for _ in range(n)]

year = 1
while True:

    if year % 2 == 1:
        current_ice = ice
        next_ice = ice2
    else:
        current_ice = ice2
        next_ice = ice

    # melt
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            next_ice[i][j] = current_ice[i][j]
            if current_ice[i - 1][j] == 0: next_ice[i][j] -= 1
            if current_ice[i + 1][j] == 0: next_ice[i][j] -= 1
            if current_ice[i][j - 1] == 0: next_ice[i][j] -= 1
            if current_ice[i][j + 1] == 0: next_ice[i][j] -= 1
            if next_ice[i][j] < 0:
                next_ice[i][j] = 0
    
    # check
    visited = [[False for _ in range(m)] for _ in range(n)]
    all_melt = True
    checked = False
    devided = False
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if next_ice[i][j] > 0 and checked and not visited[i][j]:
                devided = True
            elif next_ice[i][j] > 0 and not visited[i][j]:
                all_melt = False
                checked = True
                stack = [(i, j)]
                while len(stack) > 0:
                    temp = stack.pop()
                    visited[temp[0]][temp[1]] = True
                    for move in dir:
                        ti, tj = map(int, (t1 + t2 for t1, t2 in zip(temp, move)))
                        if next_ice[ti][tj] > 0 and not visited[ti][tj]:
                            visited[ti][tj] = True
                            stack.append((ti, tj))
    
    if all_melt:
        print(0)
        break

    if devided:
        print(year)
        break

    year += 1