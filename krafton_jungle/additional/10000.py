import sys

n = int(sys.stdin.readline())

circles = []
for _ in range(n):
    x, r = map(int, sys.stdin.readline().split())
    circles.append((x - r, r + r)) # left coordinate, dimaster

circles.sort()

cnt = 0
stack = []
for circle in circles:
    if stack and stack[0][0] + stack[0][1] <= circle[0]:
        stack.pop()
        