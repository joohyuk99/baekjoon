from queue import PriorityQueue
import sys

q = PriorityQueue()

n = int(input())

cnt = 0
for i in range(n):
    t = int(sys.stdin.readline())
    if t == 0:
        if cnt == 0:
            print(0)
        else:
            print(q.get()[1])
            cnt -= 1
    else:
        q.put((-1 * t, t))
        cnt += 1