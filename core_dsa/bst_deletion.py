class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    elif key > root.data:
        root.right = insert(root.right, key)
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current


def delete_node(root, key):
    if root is None:
        return root
    if key < root.data:
        root.left = delete_node(root.left, key)
    elif key > root.data:
        root.right = delete_node(root.right, key)
    else:
        # not found
        if root.left is None and root.right is None:
            return None
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # two children
        temp = min_value_node(root.right)
        root.data = temp.data
        root.right = delete_node(root.right, temp.data)
    return root


root = None
values = [50, 30, 70, 20, 40, 60, 80]

for val in values:
    root = insert(root, val)

print("Original BST (inorder): ")
inorder(root)

root = delete_node(root, 50)

print("\nBST afterdeleting 50(inorder): ")
inorder(root)
