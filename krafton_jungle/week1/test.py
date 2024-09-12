a= [1, 5, 232, 212, 63, 2, 7, 7, 4, 3, 6, 0, 8, 3, 12, 20, 53, 3, 124, 5]
pl = 0
pr = len(a) - 1

x = 5
#x = a[(pl + pr) // 2]
print(x)
while pl <= pr:
    while a[pl] < x: pl += 1
    while a[pr] > x: pr -= 1
    if pl <= pr:
        a[pl], a[pr] = a[pr], a[pl]
        pl += 1
        pr -= 1
    print(pl, pr, a)