import sys

n = input()
b = []
for i in range(int(n)):
    b.append(list(map(int, sys.stdin.readline().split())))

blue = 0
white = 0

def RectColor(x, y, r):
    global blue, white
    temp = b[x][y]
    for i in range(x, x + r):
        for j in range(y, y + r):
            if b[i][j] != temp:
                return -1
    if b[x][y] == 1:
        blue += 1
    else:
        white += 1

def countBlueR(x, y, r):
    t = RectColor(x, y, r)
    #print(t)
    if t == -1:
        countBlueR(x, y, r // 2)
        countBlueR(x + r // 2, y, r // 2)
        countBlueR(x, y + r // 2, r // 2)
        countBlueR(x + r // 2, y + r // 2, r // 2)

countBlueR(0, 0, int(n))
print(white)
print(blue)