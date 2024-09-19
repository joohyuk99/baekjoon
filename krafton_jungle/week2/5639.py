import sys
l = sys.stdin.readlines()

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

root = None
for v in l:
    v = int(v)
    if root == None:
        root = Node(v)
    else:
        current_node = root
        while True:
            if v < current_node.key:
                if current_node.left == None:
                    current_node.left = Node(v)
                    break
                else:
                    current_node = current_node.left
            else:
                if current_node.right == None:
                    current_node.right = Node(v)
                    break
                else: current_node = current_node.right

s = []
ans = []
s.append(root)
while len(s) != 0:
    current_node = s.pop()
    if current_node == None:
        continue
    ans.append(current_node.key)
    s.append(current_node.left)
    s.append(current_node.right)

for i in range(len(ans) - 1, -1, -1):
    print(ans[i])