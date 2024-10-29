import sys

n, k = map(int, sys.stdin.readline().split())
num = [int(i) for i in sys.stdin.readline()[:-1]]

ans = []
list_idx = 0
while list_idx < n and k > 0:
    #print("start", ans, list_idx, k)
    max_idx, max_val = list_idx, num[list_idx]
    for i in range(list_idx, list_idx + k + 1):
        if i == n:
            break
        if max_val < num[i]:
            max_val = num[i]
            max_idx = i
    ans.append(max_val)
    k -= max_idx - list_idx
    list_idx = max_idx + 1
    #print("end", ans, list_idx, k)

if k > 0:
    for i in range(k):
        ans.pop()
else:
    for i in range(list_idx, n):
        ans.append(num[i])

for val in ans:
    print(val, end="")
print("")