import sys

n = int(sys.stdin.readline())
land = []
for i in range(n):
    land.append(list(map(int, sys.stdin.readline().split())))

maximum = -1
for rain in range(100):
    isFlood = [[0 for _ in range(n)] for _ in range(n)] # 0 flood / 1 before count / 2 counted
    for i in range(n):
        for j in range(n):
            if land[i][j] > rain:
                isFlood[i][j] = 1
    
    cnt = 0
    for i in range(n):
        for j in range(n):
            if isFlood[i][j] == 1:
                cnt += 1
                stack = []
                stack.append((i, j))
                isFlood[i][j] = 2
                while len(stack):
                    temp = stack.pop()
                    if temp[0] != 0 and isFlood[temp[0] - 1][temp[1]] == 1:
                        isFlood[temp[0] - 1][temp[1]] = 2
                        stack.append((temp[0] - 1, temp[1]))
                    if temp[1] != 0 and isFlood[temp[0]][temp[1] - 1] == 1:
                        isFlood[temp[0]][temp[1] - 1] = 2
                        stack.append((temp[0], temp[1] - 1))
                    if temp[0] != n - 1 and isFlood[temp[0] + 1][temp[1]] == 1:
                        isFlood[temp[0] + 1][temp[1]] = 2
                        stack.append((temp[0] + 1, temp[1]))
                    if temp[1] != n - 1 and isFlood[temp[0]][temp[1] + 1] == 1:
                        isFlood[temp[0]][temp[1] + 1] = 2
                        stack.append((temp[0], temp[1] + 1))

    maximum = max(maximum, cnt)

print(maximum)