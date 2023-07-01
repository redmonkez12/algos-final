class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = Node(7)
root.left = Node(23)
root.right = Node(8)
root.left.left = Node(5)
root.left.right = Node(4)
root.right.left = Node(21)
root.right.right = Node(15)

"""
    Root - 7

        7
       / \
     23    8
    / \   / \
   5  4  21 15
"""

# def dfs_search(node, target):
#     if node is None:
#         return False
#
#     if node.value == target:
#         return True
#
#     # Recursive search in the left subtree
#     if dfs_search(node.left, target):
#         return True
#
#     # Recursive search in the right subtree
#     if dfs_search(node.right, target):
#         return True
#
#     return False


def dfs_search(node, target):
    if node is None:
        return False

    stack = [node]

    while stack:
        current = stack.pop()

        if current.value == target:
            return True

        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)

    return False


result = dfs_search(root, 21)
print(result)