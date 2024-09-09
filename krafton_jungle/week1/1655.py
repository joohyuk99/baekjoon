import sys
import heapq

n = int(sys.stdin.readline())

front_heap = []
back_heap = []

mid = int(sys.stdin.readline())
print(mid)
for idx in range(n - 1):
    buf = int(sys.stdin.readline())
    if idx % 2 == 1:
        if buf < mid:
            temp = buf
            buf = mid
            mid = temp
        heapq.heappush(front_heap, buf * -1)
    else:
        if buf > mid:
            temp = buf
            buf = mid
            mid = temp
        heapq.heappush(back_heap, buf)

    if idx == 0:
        if mid > back_heap[0]:
            temp = mid
            mid = heapq.heappop(back_heap)
            heapq.heappush(back_heap, temp)
    else:
        while not (front_heap[0] * -1 <= mid and mid <= back_heap[0]):
            if mid < front_heap[0] * -1:
                temp = mid
                mid = heapq.heappop(front_heap) * -1
                heapq.heappush(front_heap, temp * -1)
            if mid > back_heap[0]:
                temp = mid
                mid = heapq.heappop(back_heap)
                heapq.heappush(back_heap, temp)
    #print(front_heap, mid, back_heap)
    print(mid)