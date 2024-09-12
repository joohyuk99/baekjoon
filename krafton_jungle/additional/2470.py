import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

l.sort()
m = (0, 1)
for idx, val in enumerate(l):
    s = idx + 1
    e = len(l) - 1
    p = val * -1
    mid = (s + e) // 2
    while s <= e:
        #print(idx, s, e, mid, l[mid])
        mid = (s + e) // 2
        if l[mid] == p:
            break
        elif l[mid] > p:
            e = mid - 1
        else:
            s = mid + 1
    if mid != idx:
        if abs(l[m[0]] + l[m[1]]) > abs(val + l[mid]):
            #print(f"mid: {m}, {idx}, {val}, {mid}")
            m = (idx, mid)
    if mid - 1 >= 0 and mid - 1 != idx:
        if abs(l[m[0]] + l[m[1]]) > abs(val + l[mid - 1]):
            #print(f"mid - 1: {m}, {idx}, {val}, {mid - 1}")
            m = (idx, mid - 1)
    if mid + 1 < n and mid + 1 != idx:
        if abs(l[m[0]] + l[m[1]]) > abs(val + l[mid + 1]):
            #print(f"mid + 1: {m}, {idx}, {val}, {mid + 1}")
            m = (idx, mid + 1)

print(l[m[0]], l[m[1]])