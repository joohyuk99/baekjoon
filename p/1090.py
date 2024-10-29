import sys

n = int(sys.stdin.readline())

list_i = []
list_j = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    list_i.append(a)
    list_j.append(b)

for k in range(1, n + 1):
    

ti = sum(list_i) // len(list_i)
tj = sum(list_j) // len(list_j)

for idx in range(n):
    print(abs(list_i[idx] - ti) + abs(list_j[idx] - tj), end=" ")

print()
print(ti, tj)
print(list_i, list_j)