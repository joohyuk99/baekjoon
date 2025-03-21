from collections import deque

def solution(queue1, queue2):
    q = queue1 + queue2
    l = len(q)
    g = sum(q)
    if g % 2 == 1:
        return -1
    g = g // 2
        
    left, right = 0, len(queue1)
    s = sum(queue1)
    loop = 0
    while True:
        if loop > l * 2 or left > right:
            return -1
        if s == g:
            break
        elif s > g:
            s -= q[left]
            left += 1
            if left == l:
                left = 0
        elif s < g:
            s += q[right]
            right += 1
            if right == l:
                right = 0
        loop += 1
    return loop