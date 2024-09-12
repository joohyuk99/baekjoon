import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

t = b
for i in range(3):
    print(a * (t % 10))
    t = t // 10
print(a * b)