import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
op = tuple(map(int, sys.stdin.readline().split()))

stack = [(op, a[0], 1)] # (plus, minus, multuple, divide), cal, index
maximum = -1000000000
minimum = 1000000000
while len(stack) > 0:
    temp = stack.pop()
    #print(temp)
    if temp[0] == (0, 0, 0, 0):
        maximum = max(maximum, temp[1])
        minimum = min(minimum, temp[1])
    else:
        if temp[0][0] > 0:
            stack.append((tuple(sum(val) for val in zip(temp[0], (-1, 0, 0, 0))), temp[1] + a[temp[2]], temp[2] + 1))
        if temp[0][1] > 0:
            stack.append((tuple(sum(val) for val in zip(temp[0], (0, -1, 0, 0))), temp[1] - a[temp[2]], temp[2] + 1))
        if temp[0][2] > 0:
            stack.append((tuple(sum(val) for val in zip(temp[0], (0, 0, -1, 0))), temp[1] * a[temp[2]], temp[2] + 1))
        if temp[0][3] > 0:
            if temp[1] < 0:
                temp2 = ((temp[1] * -1) // a[temp[2]]) * -1
            else:
                temp2 = temp[1] // a[temp[2]]
            stack.append((tuple(sum(val) for val in zip(temp[0], (0, 0, 0, -1))), temp2, temp[2] + 1))

print(maximum)
print(minimum)