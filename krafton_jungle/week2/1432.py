from collections import deque
import heapq
import sys

n = int(sys.stdin.readline())
edge = [set() for _ in range(n)] # edge[i][j] => j → i arc
outdegree = [0 for _ in range(n)]

for i in range(n):
    buf = sys.stdin.readline()
    for j in range(n):
        if buf[j] == '1':
            edge[j].add(i)
            outdegree[i] += 1

heap = []
for idx, val in enumerate(outdegree):
    if val == 0:
        heapq.heappush(heap, -1 * idx)

ans = deque()
while len(heap) > 0:
    current_node = heapq.heappop(heap) * -1
    ans.appendleft(current_node)

    for next_node in edge[current_node]:
        outdegree[next_node] -= 1
        if outdegree[next_node] == 0:
            heapq.heappush(heap, -1 * next_node)

if len(ans) != n:
    print(-1)
else:
    print_list = [None for _ in range(n)]
    for idx, val in enumerate(ans):
        print_list[val] = idx + 1
    for val in print_list:
        print(val, end=" ")
    print("")