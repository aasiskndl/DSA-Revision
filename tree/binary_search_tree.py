"""binary search tree is a special kind of binary tree where:
1. left subtree contains nodes with value less than that of the root
2. right subtree contains the nodes with values greater than the root
3. if we divide them to individual trees i.e. left subtree and right subtree ten they are also binary trees individually
"""


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


def search(root, key):
    if root is None or root.data == key:
        return root
    if key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# example usage
root = None
values = [50, 30, 70, 20, 40, 60, 80]

for val in values:
    root = insert(root, val)

print("Inorder traversal of BST:")
inorder(root)

# search for a key
key = 19
found = search(root, key)
if found:
    print(f"\n{key} found in BST")

else:
    print(f"\n{key} not found in BST")
