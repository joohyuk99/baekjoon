import sys

buf = sys.stdin.readline()
temp_num = 0
ans = 0
isMinus = False
for val in buf:
    if val == '+' or val == '-' or val == '\n':

        if not isMinus:
            ans += temp_num
        else:
            ans -= temp_num
        
        if val == '-':
            isMinus = True
        
        temp_num = 0
    
    else:
        temp_num = temp_num * 10 + int(val)

print(ans)