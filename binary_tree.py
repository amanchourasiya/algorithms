class Node():
    def __init__(self,data:int):
        self.data = data
        self.left = None
        self.right = None


'''
Inserts a new node into an existing binary tree
Params
root: Root node of binary tree
node: Node to be inserted
'''
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

'''
Wrapper function around insert_node function which reduces the creation of new node every time
'''
def insert(root,data):
    node = Node(data)
    insert_node(root,node)

'''
Function to traverse a binary search tree inorder
'''
def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)

def postorder(root):
    if root == None:
        return
    
    postorder(root.left)
    postorder(root.right)
    print(root.data)

def preorder(root):
    if root == None:
        return
    print(root.data)
    preorder(root.left)
    preorder(root.right)

def search(root,element):
    if root == None:
        return -1
    if element == root.data:
        return 1
    elif element < root.data:
        return search(root.left,element)
    else:
        return search(root.right,element)

def is_mirror(root):
    # Checking base case
    if root is None:
        return True
    
    # If only one element in tree then its mirror
    if root.left is None and root.right is None:
        return True
    return check_mirror(root.left,root.right)

def check_mirror(left_subtree,right_subtree):
    if left_subtree is None and right_subtree is None:
        return True
    if (left_subtree is None and right_subtree is not None) or (left_subtree is not None and right_subtree is None):
        return False
    return(check_mirror(left_subtree.left,right_subtree.right) and check_mirror(left_subtree.right,right_subtree.left))



'''
Test function to test basic functinality of various tree operations
'''
def test():
    root = Node(10)
    elements = [4,1,6,5,15,12,13,16]
    for element in elements:
        insert(root,element)
    inorder(root)
    print(is_mirror(root))
test()
        