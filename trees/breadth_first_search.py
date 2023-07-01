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


def breadth_search(root, value):
    queue = [root]

    while len(queue):
        curr = queue.pop(0)  # {"node": 21, "level": 0}

        if curr.value == value:  # 21 == 21
            return True

        if curr.left:
            queue.append(curr.left)  # [15]

        if curr.right:
            queue.append(curr.right)  # [15]

    return False


result = breadth_search(root, 21)
print(result)
