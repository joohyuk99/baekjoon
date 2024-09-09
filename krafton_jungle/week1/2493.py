import sys
n = int(input())
t = list(map(int, sys.stdin.readline().split()))

stack = []
for idx, v in enumerate(t):
    if not len(stack):
        print("0 ", end="")
        stack.append((v, idx))
    else:
        while True:
            if not len(stack):
                print("0 ", end="")
                stack.append((v, idx))
                break
            elif stack[-1][0] < v:
                stack.pop()
            elif stack[-1][0] == v:
                print(f"{stack[-1][1] + 1} ", end="")
                stack.pop()
                stack.append((v, idx))
                break
                
            else:
                print(f"{stack[-1][1] + 1} ", end="")
                stack.append((v, idx))
                break