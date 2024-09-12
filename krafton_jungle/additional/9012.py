import sys
n = int(sys.stdin.readline())
for _ in range(n):
    t = sys.stdin.readline()
    s = []
    for v in t:
        #print(s, v)
        if v == '(':
            s.append(v)
        elif v == ')':
            if len(s) == 0:
                s.append(None)
                break
            elif s[-1] != '(':
                break
            else:
                s.pop()
    if len(s) == 0:
        print("YES")
    else:
        print("NO")