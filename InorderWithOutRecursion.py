#inorder traversal = left,root,right -> with out recursion using stack

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def height(root):
    if root is None:
        return 0
    else:
        return 1+max(height(root.left),height(root.left))