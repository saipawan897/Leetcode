#inorder traversal = left,root,right -> with out recursion using stack

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def inorder(root):
    