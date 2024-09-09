from collections import deque
import sys

LEFT = (0, -1)
RIGHT = (0, 1)
UP = (-1, 0)
DOWN = (1, 0)

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

board = [[0 for _ in range(n)] for _ in range(n)]

for i in range(k):
    a, b = map(int, sys.stdin.readline().split())
    board[a - 1][b - 1] = 1 # apple

l = int(sys.stdin.readline())
rotate = []
for i in range(l):
    a, b = sys.stdin.readline().split()
    rotate.append((int(a), b))

time = 0
rotate_idx = 0

snake = deque()
snake.append((0, 0))

current_dir = RIGHT

last_dir = [LEFT, RIGHT, UP, DOWN]
L_dir = {LEFT: DOWN, RIGHT: UP, UP: LEFT, DOWN: RIGHT}
D_dir = {LEFT: UP, RIGHT: DOWN, UP: RIGHT, DOWN: LEFT}
def rotate_snake(last_dir, rot):
    if rot == 'L':
        return L_dir[last_dir]
    else:
        return D_dir[last_dir]

def print_board():
    global time, current_dir
    print(time, current_dir)
    for val in snake:
        board[val[0]][val[1]] = 2
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                print("- ", end="")
            elif board[i][j] == 1:
                print("O ", end="")
            elif board[i][j] == 2:
                print("+ ", end="")
        print("")
    print("")

while True:
    # next location
    temp = (snake[0][0] + current_dir[0], snake[0][1] + current_dir[1])
    
    # check game is over
    if -1 in temp or n in temp:
        break
    if temp in snake:
        break

    # check apple
    if board[temp[0]][temp[1]] != 1:
        temp2 = snake.pop()
        board[temp2[0]][temp2[1]] = 0

    # move
    snake.appendleft(temp)
    board[temp[0]][temp[1]] = 2

    # rotate
    if rotate_idx != l and rotate[rotate_idx][0] - 1 == time:
        current_dir = rotate_snake(current_dir, rotate[rotate_idx][1])
        rotate_idx += 1

    time += 1

    #print_board()

print(time + 1)