from collections import deque
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

# input
road_start = [{} for _ in range(n)]
road_end = [set() for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    road_start[a - 1][b - 1] = c
    road_end[b - 1].add(a - 1)
start, destination = map(int, sys.stdin.readline().split())

path = [-1 for _ in range(n)] # time
road = [set() for _ in range(n)] # tuple set, (start node, end node)
queue = deque()
queue.append(start - 1) # node, time, road_number
path[start - 1] = 0
while len(queue) > 0:
    current_node = queue.popleft()
    current_time = path[current_node]
    for next_node, time in road_start[current_node].items():
        if path[next_node] < current_time + road_start[current_node][next_node]:
            path[next_node] = current_time + road_start[current_node][next_node]
            road[next_node] = road[current_node].copy()
            road[next_node].add((current_node, next_node))
        elif path[next_node] == current_time + road_start[current_node][next_node]:
            road[next_node] |= road[current_node]
            road[next_node].add((current_node, next_node))
        road_end[next_node].discard(current_node)
        if len(road_end[next_node]) == 0:
            queue.append(next_node)
    if current_node != destination - 1:
        road[current_node] = None
    #print(current_node, path)

print(path[destination - 1])
print(len(road[destination - 1]))