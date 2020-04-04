class Node():
    def __init__(self,data:int):
        self.data = data
        self.left = None
        self.right = None

def insert_node(root,node):
    if root == None:
        return node
    if node.data < root.data:
        if root.left == None:
            root.left = node
        else:
            root.left = insert_node(root.left,node)
    else:
        if root.right == None:
            root.right = node
        else:
            root.right = insert_node(root.right,node)

    return root

def insert(root,data):
    node = Node(data)
    insert_node(root,node)

def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)

def test():
    root = Node(10)
    insert(root,1)
    insert(root,2)
    insert(root,23)
    insert(root,34)
    inorder(root)

test()
        