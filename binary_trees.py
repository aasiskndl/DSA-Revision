# a tree is a non-linear data structure made of nodes connected by edges
# each node contains: data and references to child nodes

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right= None
        
        
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
        
def preorder(root):
    if root:
        print(root.data, end= " ")
        preorder(root.left)
        preorder(root.right)
        
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end = " ")
        
#creating nodes
root = Node(1)
root.left = Node(2)
root.right= Node(3)

root.left.left = Node(4)
root.left.right = Node(5)
        
        
# printing the trees
print("Inorder Teaversal: ")
inorder(root)

print("\nPreorder Traversal: ")
preorder(root)

print("\nPostorder Traversal")
postorder(root)