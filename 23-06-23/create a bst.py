class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root

def search(root, key):
    if root is None or root.data == key:
        return root
    if root.data < key:
        return search(root.right, key)
    return search(root.left, key)

# Create a binary search tree from the given list
def createBST(nums):
    root = None
    for num in nums:
        root = insert(root, num)
    return root

# Given list
nums = [100, 70, 50, 60, 9, -3]

# Create the binary search tree
bst = createBST(nums)

# Perform search operation
search_key = 60
result = search(bst, search_key)
if result is not None:
    print(f"Element {search_key} found in the BST")
else:
    print(f"Element {search_key} not found in the BST")
