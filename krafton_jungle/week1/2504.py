import sys
data = sys.stdin.readline()
stack = []

def isCorrect():
    for v in data:
        if v == '(' or v == '[':
            stack.append(v)
        elif v == ']':
            if len(stack) == 0:
                return False
            t = stack.pop()
            if t != '[':
                return False
        elif v == ')':
            if len(stack) == 0:
                return False
            t = stack.pop()
            if t != '(':
                return False
    if len(stack) != 0:
        return False
    return True

def calc():
    for val in data:
        if val == '(' or val == '[':
            stack.append(val)
        else:
            buf = 0
            while True:
                if len(stack) == 0:
                    stack.append(buf)
                    break
                t = stack.pop()
                if t == '(' and val == ')':
                    if buf == 0:
                        stack.append(2)
                    else:
                        stack.append(2 * buf)
                    break
                elif t == '[' and val == ']':
                    if buf == 0:
                        stack.append(3)
                    else:
                        stack.append(3 * buf)
                    break
                else:
                    buf += t
    return 


if not isCorrect():
    print("0")
else:
    calc()
    print(stack[0])