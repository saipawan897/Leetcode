
# BFS vs DFS for Binary Tree
"""
Bredth First Search - Level Order Traversal - Queues are used
Depth First Search - Inorder, Preorder, PostOder traversal - stacks are use

When searching is closer to root then BFS is prefered as the searching happens from root to lead
When searching is closer to leaf then DFS is prefered as the searching happens from the leaf to root
"""

#Level Order traversal - 2 methods 1) Using priniting current ndoe val 2) Using queues

#Method 1:

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
    
def print_level_order(root):
    h = height(root)
    for i in range(1,h+1):
        print_current_level(root,i)

def print_current_level(root, level):
    if root is None:
        return
    if level == 1:
        print(root.val,end =  "   ")
    elif level > 1:
        print_current_level(root.left, level-1)
        print_current_level(root.right, level-1)

def height(node):
    if node is None:
        return 0

    else:
        lheight = height(node.left)
        rheight = height(node.right)
        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
print("Level order traversal of binary tree is -")
print_level_order(root)

