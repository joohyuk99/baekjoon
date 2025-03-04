import sys

num = int(sys.stdin.readline())

s = set()
for _ in range(num):

    l = sys.stdin.readline().split()

    if l[0] == "all":
        for i in range(1, 21):
            s.add(i)
    
    if l[0] == "empty":
        s = set()
    
    if l[0] == "add":
        n = int(l[1])
        if n not in s:
            s.add(n)
    
    if l[0] == "remove":
        n = int(l[1])
        if n in s:
            s.remove(n)
    
    if l[0] == "check":
        n = int(l[1])
        if n in s:
            print(1)
        else:
            print(0)
    
    if l[0] == "toggle":
        n = int(l[1])
        if n in s:
            s.remove(n)
        else:
            s.add(n)