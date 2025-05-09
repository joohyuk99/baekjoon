for test_case in range(1, 11):
    n = int(input())
    l = list(map(int, input().split()))
    s = 0
    for i in range(2, n - 2):
        m = -1
        m = max(m, l[i - 2])
        m = max(m, l[i - 1])
        m = max(m, l[i + 2])
        m = max(m, l[i + 1])
        if l[i] > m:
            s = s + l[i] - m
    print(f"#{test_case} {s}")