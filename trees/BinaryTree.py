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

# [7, 23, 5, 4, 8, 21, 15]
# pre order
# def walk(curr, path):
#     if curr is None:
#         return path
#
#     # Chceme in order, pre order nebo post order
#     path.append(curr.value)
#
#     walk(curr.left, path)
#     walk(curr.right, path)
#
#     return path

# in order - leva cast, koren a prava cast
# def walk(curr, path):
#     if curr is None:
#         return path
#
#     walk(curr.left, path)  #
#
#     path.append(curr.value)  #
#
#     walk(curr.right, path)  #
#
#     return path

# post order - leva cast, prava a koren
# def walk(curr, path):
#     if curr is None:
#         return path
#
#     # Chceme in order, pre order nebo post order
#     walk(curr.left, path)  # 23 -> 5 curr = 5
#     walk(curr.right, path)  # curr.right = Non
#
#     path.append(curr.value) # 5
#
#     return path
