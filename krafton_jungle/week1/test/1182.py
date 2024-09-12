import sys

# input
n, s = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))

stack = []

# append len == 1 list
for idx, val in enumerate(l):
    stack.append((idx, val)) # (last_index, sum)

# check all case
# loop before stack is emply
cnt = 0
while len(stack) != 0:
    temp = stack.pop()
    
    if temp[1] == s:
        cnt += 1

    for idx in range(temp[0] + 1, n):
        # append new element in stack
        stack.append((idx, temp[1] + l[idx]))

print(cnt)