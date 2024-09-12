from collections import deque
import sys

n = int(sys.stdin.readline())
pic = []
for idx in range(n):
    temp_str = sys.stdin.readline()
    pic.append(list(temp_str))

for i in range(n):
    for j in range(n):
        pic[i][j] = int(pic[i][j])

# check if all dot is same
def allSame(start_dot, length): # start_dot : (int, int), length : 2 << x
    val = pic[start_dot[0]][start_dot[1]]
    for i in range(start_dot[0], start_dot[0] + length):
        for j in range(start_dot[1], start_dot[1] + length):
            if pic[i][j] != val:
                # return -1 if all dot is not same
                return -1
    return val

ans = []
# solve function
def solve(start_dot, length): # start_dot : (int, int), length : 2 << x
    
    #if length is 1, end recursion
    if length == 1:
        ans.append(pic[start_dot[0]][start_dot[1]])
        return 
    
    temp = allSame(start_dot, length)
    # if all dot is not same
    if temp == -1:
        ans.append('(')
        solve(start_dot, length // 2)
        solve((start_dot[0], start_dot[1] + length // 2), length // 2)
        solve((start_dot[0] + length // 2, start_dot[1]), length // 2)
        solve((start_dot[0] + length // 2, start_dot[1] + length // 2), length // 2)
        ans.append(')')

    # if all dot is same
    else:
        ans.append(temp)

solve((0, 0), n)
for v in ans:
    print(v, end="")
print("")