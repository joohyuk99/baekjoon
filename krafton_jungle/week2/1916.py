import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
bus = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    bus[a - 1].append((b - 1, c))
start, end = map(int, sys.stdin.readline().split())
#print(bus)
cost = [sys.maxsize for _ in range(n)]
cost[start - 1] = 0
q = [(0, start - 1)] # cost, next node
visited = [False for _ in range(n)]
while len(q) > 0:
    current_cost, current_node = heapq.heappop(q)

    if visited[current_node]:
        continue
    else:
        visited[current_node] = True

    if current_node == end - 1:
        break

    for val in bus[current_node]:
        #print(current_node, current_cost, val)
        if current_cost + val[1] < cost[val[0]]:
            cost[val[0]] = current_cost + val[1]
            if not visited[val[0]]:
                heapq.heappush(q, (current_cost + val[1], val[0]))
            #print(current_node, current_cost, val, cost, q)
    #print(current_node, cost)

print(cost[end - 1])