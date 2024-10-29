import sys
import heapq

n = int(sys.stdin.readline())

meetings = []
for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    heapq.heappush(meetings, (end, start))

ans = 0
ending_time = 0
while meetings:
    current_meeting_end, current_meeting_start = heapq.heappop(meetings)
    if ending_time <= current_meeting_start:
        ans += 1
        ending_time = current_meeting_end

print(ans)