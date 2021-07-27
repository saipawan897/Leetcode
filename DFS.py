class Node:
    def __init__(self,key):
        self.left = None
        self.right= None
        self.val = key


def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)
        if lheight>rheight:
            return lheight+1
        else:
            return rheight+1

def current_level(root,level):
    if root is None:
        return
    elif level == 1:
        print(root.val, end = "")
    else:
        current_level(root.left,level-1)
        current_level(root.right,level-1)

def level_roder(root):
    h = height(root)
    for i in range(1,h+1):
        current_level(root,i)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
print("Level order traversal of binary tree is -")
level_roder(root)

#Method using Queue

def print_level_order(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    while(len(queue) > 0):
        print(queue[0].val)
        node = queue.pop(0)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
print ("Level Order Traversal of binary tree is -")
print_level_order(root)