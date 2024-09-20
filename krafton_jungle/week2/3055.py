from collections import deque
import sys

EMPTY = '.'
WATER = '*'
STONE = 'X'
DESTINATION = 'D'
VISITED = 'S'
DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]

water = deque()
hedgehog = deque()

# input
r, c = map(int, sys.stdin.readline().split())
field = [[] for _ in range(r)]
for i in range(r):
    buf = sys.stdin.readline()
    for j in range(len(buf) - 1):
        if buf[j] == WATER:
            water.append((i, j))
            field[i].append(WATER)
        elif buf[j] == STONE:
            field[i].append(STONE)
        elif buf[j] == DESTINATION:
            field[i].append(DESTINATION)
        elif buf[j] == VISITED:
            hedgehog.append((i, j))
            field[i].append(VISITED)
        else:
            field[i].append(EMPTY)

def isValidIndex(coordinate):
    i = coordinate[0]
    j = coordinate[1]
    if i == -1 or i == r:
        return False
    if j == -1 or j == c:
        return False
    return True

cnt = 0
while len(hedgehog) > 0:
    cnt += 1

    # water spread
    for _ in range(len(water)):
        current_water = water.popleft()
        for move in DIR:
            next_index = tuple(i + j for i, j in zip(current_water, move))
            if isValidIndex(next_index):
                next_water = field[next_index[0]][next_index[1]]
                if next_water == EMPTY or next_water == VISITED:
                    water.append(next_index)
                    field[next_index[0]][next_index[1]] = WATER
    
    # move hedgehog
    for _ in range(len(hedgehog)):
        current_location = hedgehog.popleft()
        for move in DIR:
            next_index = tuple(i + j for i, j in zip(current_location, move))
            if isValidIndex(next_index):
                next_location = field[next_index[0]][next_index[1]]
                if next_location == DESTINATION:
                    print(cnt)
                    sys.exit()
                elif next_location == EMPTY:
                    hedgehog.append(next_index)
                    field[next_index[0]][next_index[1]] = VISITED

print("KAKTUS")