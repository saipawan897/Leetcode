# Diameter of a tree or width of a tree is the num of nodes on the longest path between two end nodes. The count inclues the 2 end leaf nodes

class Node:
    def __init__(self,key):
        self.left=None
        self.right= None
        self.val = key

def height(node):
    if node is None:
        return 0
    return 1+ max(height(node.left),height(node.right))
def diameter(root):
    if root is None:
        return 0
    lheight = height(root.left)
    rheight = height(root.right)
    ldia = diameter(root.left)
    rdia = diameter(root.right)
    return max(lheight+rheight + 1, max(ldia,rdia))

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
# Function Call
print(diameter(root))