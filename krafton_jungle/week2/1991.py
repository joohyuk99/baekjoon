import sys

n = int(sys.stdin.readline())

tree = [[-1, -1] for _ in range(n)]
for _ in range(n):
    a, b, c = map(str, sys.stdin.readline().split())
    if b != '.':
        tree[ord(a) - ord('A')][0] = ord(b) - ord('A')
    if c != '.':
        tree[ord(a) - ord('A')][1] = ord(c) - ord('A')

def front(current_node):
    print(f"{chr(current_node + ord('A'))}", end="")
    if tree[current_node][0] != -1:
        front(tree[current_node][0])
    if tree[current_node][1] != -1:
        front(tree[current_node][1])

def middle(current_node):
    if tree[current_node][0] != -1:
        middle(tree[current_node][0])
    print(f"{chr(current_node + ord('A'))}", end="")
    if tree[current_node][1] != -1:
        middle(tree[current_node][1])



def back(current_node):
    if tree[current_node][0] != -1:
        back(tree[current_node][0])
    if tree[current_node][1] != -1:
        back(tree[current_node][1])
    print(f"{chr(current_node + ord('A'))}", end="")


front(0)
print("")
middle(0)
print("")
back(0)
print("")