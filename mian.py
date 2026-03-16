class Tree():
    def __init__(self,x):
        self.data = x
        self.left = None
        self.right = None

def in_order(root):
    if root:
        if root.left:
            in_order(root.left)
        print(root.data)
    
        if root.right:
            in_order(root.right)

def insert(root,key):
    if root == None:
        return Tree(key)
    if key < root.data:
        root.left = insert(root.left,key)
    
    else:
        root.right = insert(root.right,key)

    return root

def search(root,key):
    if root.data == key:
        return root
    elif key < root.data and root.left != None:
        return search(root.left,key)
    elif key > root.data and root.right != None:
        return search(root.right,key)
    else:
        return -1 
    
u1 = int(input("How many node do you want in the tree? "))
root = None

for i in range(u1):
    x=int(input("What is this node's value? : "))
    root = insert(root,x)
    
in_order(root)

u2 = int(input("What number would you like to search for? "))
key_node = search(root,u2)

if key_node == -1:
    print("Node value not found")
else:
    print("Node exists",key_node.data)