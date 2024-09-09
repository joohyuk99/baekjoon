import heapq
import sys
n = int(sys.stdin.readline())

l = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    l.append((min(a, b), max(a, b)))

d = int(sys.stdin.readline())

l.sort()
#print(l)
maximun = 0
cnt = 0
count = {} # key = index
end = 0
notCount = []
for idx, val in enumerate(l):

    if end < idx:
        end += 1

    #print(f"while: {end} {val}")
    #print(notCount)
    while end < n and l[end][0] < val[0] + d:
        if l[end][1] <= val[0] + d:
            cnt += 1
            count[end] = True
            #print(idx, end, count)
        else:
            heapq.heappush(notCount, (l[end][1], l[end][0], end))
        end += 1
        #print(end - 1)

    while len(notCount) != 0 and notCount[0][0] <= val[0] + d:
        temp = heapq.heappop(notCount)
        if val[0] <= temp[1] and temp[0] <= val[0] + d:
            cnt += 1
            count[temp[2]] = True


    #while len(notCount) != 0 and notCount[0][0] < val[0]:
    #    heapq.heappop(notCount)
    ##print(notCount)
    #for idx2 in reversed(range(len(notCount))):
    #    #print(f"notCount : {notCount[idx2]} {val[0] + d}")
    #    if notCount[idx2][1] <= val[0] + d:
    #        cnt += 1
    #        count[notCount[idx2][2]] = True
    #        notCount.pop(idx2)

    #print("after: ", end="")
    #print(idx, cnt, count)
    #print("")
    maximun = max(maximun, len(count))

    if idx in count:
        count.pop(idx)
        cnt -= 1

print(maximun)