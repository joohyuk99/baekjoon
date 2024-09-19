import sys

test_case = int(sys.stdin.readline())
for _ in range(test_case):
    u, v = map(int, sys.stdin.readline().split())
    edge = [[] for _ in range(u)]
    for _ in range(v):
        a, b = map(int, sys.stdin.readline().split())
        edge[a - 1].append(b - 1)
        edge[b - 1].append(a - 1)
    group = [-1 for _ in range(u)]
    ans = "YES"
    for sn in range(u):
        if group[sn] == -1:
            group[sn] = True
            stack = [sn]
            while len(stack) > 0:
                current_node = stack.pop()
                for next_node in edge[current_node]:
                    if group[next_node] == -1:
                        group[next_node] = not group[current_node]
                        stack.append(next_node)
                    elif group[next_node] == group[current_node]:
                        ans = "NO"
                        break
        if ans == "NO":
            break
    print(ans)