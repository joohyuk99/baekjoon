T = int(input())
for testcase in range(1, T + 1):
    l = list(map(int, input().split()))
    s = 0
    for e in l:
        if e % 2 == 1:
            s = s + e
    print(f"#{testcase} {s}")