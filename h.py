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



def search_lrg(root):
    if root == None:
       return None
    while root.right is not None:
       root = root.right
    
    return root.data








root = None
x=2
for i in range(5):
    x=x*2
    root = insert(root,x)
    
in_order(root)

max_value =search_lrg(root)
print("Max Value : BST =",max_value)