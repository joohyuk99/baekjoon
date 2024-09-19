import sys

n = int(sys.stdin.readline())

inside = []
outside = []
node = [None for _ in range(n)]
temp = sys.stdin.readline()
for i in range(len(temp) - 1):
    if int(temp[i]) == 1:
        inside.append(i)
        node[i] = True
    else:
        outside.append(i)
        node[i] = False

tree = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    tree[u - 1].append(v - 1)
    tree[v - 1].append(u - 1)

ans = (n - 1) * 2
check = [False for _ in range(n)]
for val in outside:
    if not check[val]:
        if tree[val] == 1:
            ans -= 1
        else:
            cnt = 0
            stack = [val]
            while len(stack) > 0:
                temp = stack.pop()
                check[temp] = True
                for val2 in tree[temp]:
                    if node[val2]:
                        ans -= 2
                        cnt += 1
                    elif not check[val2]:
                        ans -= 2
                        stack.append(val2)
            ans += cnt * (cnt - 1)

print(ans)