#Trees are hierarchical data structure 
#searching : Faster than linkedlist and slower than arrays
"""
Full Binary Tree: A binary tree with every node has 0 or 2 children 
Complete Binary Tree: A binary tree is a complete binary tree if all levels are completely filled except last level
perfect Binary Tree: A Binary Tree is a perfect binary tree in which all internal nodes have two children and all leaf nodes are the same level
Balanced Binary Tree: A binary Tree is balance if he height of the tree is O(logN) where n is num of nodes
"""

"""
Applications of Tree data structure: 1) Search for key Insertion in moiderate time
"""

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
"""
Tree Traversal : 
1) Inorder(left, root, right)
2) Preorder(root,left,right)
3)postorder(left,right,root)
"""

def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.val)
        print_inorder(root.right)

def print_preorder(root):
    if root:
        print(root.val)
        print_preorder(root.left)
        print_preorder(root.right)

def print_postorder(root):
    if root:
        print_postorder(root.left)
        print_postorder(root.right)
        print(root.val)



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
print("In order traversal")
print_inorder(root)
print("Preorder traversal")
print_preorder(root)
print("Post Order Traversal")
print_postorder(root)

