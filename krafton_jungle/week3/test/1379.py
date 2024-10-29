import sys
import heapq

n = int(sys.stdin.readline())

classes = []
for _ in range(n):
    num, start, end = map(int, sys.stdin.readline().split())
    classes.append((start, 1, num)) # start
    classes.append((end, 0, num)) # end

classes.sort(key=lambda x:(x[0], x[1]))

s = {} # class - classroom
maxi = 0

empty_classroom = set()

ans = [None for _ in range(n + 1)]

for v in classes:
    if v[1] == 1:
        if len(empty_classroom) == 0:
            empty_classroom.add(maxi + 1)
        classroom = empty_classroom.pop()
        s[v[2]] = classroom
        ans[v[2]] = classroom
        maxi = max(maxi, len(s))

    elif v[1] == 0:
        classroom = s.pop(v[2])
        empty_classroom.add(classroom)
    
print(maxi)
for v in ans[1:]:
    print(v)