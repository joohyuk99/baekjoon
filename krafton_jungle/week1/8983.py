import sys
m, n, l = map(int, sys.stdin.readline().split())

li = []
temp = list(map(int, sys.stdin.readline().split()))
for i in temp:
    li.append((i, -1))

for i in range(n): 
    a, b = map(int, sys.stdin.readline().split())
    if b <= l:
        li.append((a - (l - b), i, 0))
        li.append((a + (l - b), i, 1)) # i animal

li.sort()

animal_dict = {}

cnt = 0
flag_x = -1
for v in li:


    if v[1] == -1:
        cnt += len(animal_dict)
        flag_x = v[0]
        animal_dict = {}
    elif flag_x == v[0]:
        if v[2] == 0:
            cnt += 1
    else:
        if v[2] == 0:
            animal_dict[v[1]] = True
        else:
            if v[1] in animal_dict:
                animal_dict.pop(v[1])
    #print(v)
    #print(animal_dict)
    #print(cnt)
    #print()
print(cnt)