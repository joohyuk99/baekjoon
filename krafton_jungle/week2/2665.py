from collections import deque
import sys

BLACK = -1
WHITE = -2
DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# input
n = int(sys.stdin.readline())
maze = [[] for _ in range(n)]
for i in range(n):
    buf = sys.stdin.readline()
    for j in range(n):
        if buf[j] == '0':
            maze[i].append(BLACK)
        else:
            maze[i].append(WHITE)

queue = deque()
maze[0][0] = 0
queue.append((0, 0))
while True:
    for _ in range(len(queue)):
        current_idx = queue.popleft()
        current_node = maze[current_idx[0]][current_idx[1]]
        for move in DIR:
            next_idx = tuple(i + j for i, j in zip(current_idx, move))
            if next_idx == (n - 1, n - 1):
                print(current_node)
                sys.exit()
            validIndex = True
            if -1 in next_idx or n in next_idx:
                validIndex = False
            if validIndex:
                next_node = maze[next_idx[0]][next_idx[1]]
                if next_node == BLACK:
                    maze[next_idx[0]][next_idx[1]] = current_node + 1
                    queue.append(next_idx)
                elif next_node == WHITE:
                    stack = [next_idx]
                    maze[next_idx[0]][next_idx[1]] = current_node
                    while len(stack) > 0:
                        DFS_current_node = stack.pop()
                        DFS_current_change = maze[DFS_current_node[0]][DFS_current_node[1]]
                        for DFS_move in DIR:
                            DFS_next_idx = tuple(i + j for i, j in zip(DFS_current_node, DFS_move))
                            if DFS_next_idx == (n - 1, n - 1):
                                print(DFS_current_change)
                                sys.exit()
                            DFS_validIndex = True
                            if -1 in DFS_next_idx or n in DFS_next_idx:
                                DFS_validIndex = False
                            if DFS_validIndex:
                                DFS_next_node = maze[DFS_next_idx[0]][DFS_next_idx[1]]
                                if DFS_next_node == BLACK:
                                    maze[DFS_next_idx[0]][DFS_next_idx[1]] = DFS_current_change + 1
                                    queue.append(DFS_next_idx)
                                elif DFS_next_node == WHITE:
                                    maze[DFS_next_idx[0]][DFS_next_idx[1]] = DFS_current_change
                                    stack.append(DFS_next_idx)

    # for val in maze:
    #     print(val)
    # print("")