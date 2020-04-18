import copy 

class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.isRed = True
    
    

def isRed(root):
    if root is None:
        return False
    return root.isRed


def insert(root,node):
    if root == None:
        return node
    if node.data < root.data:
        root.left = insert(root.left,node)
    elif node.data > root.data:
        root.right = insert(root.right,node)

    if (not isRed(root.left)) and isRed(root.right):
        root = rotate_left(root)
    if isRed(root.left) and isRed(root.left.left):
        root = rotate_right(root)
    if isRed(root.left) and isRed(root.right):
        root = flip_color(root)
    return root
    
def rotate_left(root):
    print('rotate left')
    root.isRed = True                # Making current (soon to be left) node as red 
    root.right.isRed = False         # Making current (soon to be root) node as black
    tmp = root.right
    root.right = root.right.left
    tmp.left = root
    root = tmp                       # Making current right as root
    
    return root

def rotate_right(root):
    print('rotate right')
    #tmp = root
    #print('root initially',root.data)
    root.isRed = True
    root.left.isRed = False
    tmp = copy.deepcopy(root.left)
    #print('tmp',tmp.data)
    root.left = root.left.right
    #print('root.left',root.left.data)
    tmp.right = root
    root = tmp
    #print('tmp right ',root.data)
    print('root last',root.right.data)
    return root

def flip_color(root):
    root.left.isRed = False
    root.right.isRed = False
    root.isRed = True
    return root


def test():
    root = Node(6)
    root = insert(root,Node(5))
    root = insert(root,Node(4))
    root = insert(root,Node(7))
    print(root.right.isRed)

test()

