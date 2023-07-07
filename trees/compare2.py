from typing import Optional

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.value}"


def compare(a: Optional[Node], b: Optional[Node]) -> bool:
    # structural check
    if a is None and b is None:
        return True

    # structural check
    if a is None or b is None:
        return False

    if a.value != b.value:
        return False

    return compare(a.left, b.left) and compare(a.right, b.right)


"""
        1
       / \
     2    3
"""

root_1 = Node(1)
root_1.left = Node(2)
root_1.right = Node(3)

"""
        1
       /
     2  
    /
   3
"""

root_2 = Node(1)
root_2.left = Node(2)
root_2.right = Node(3)

print(compare(root_1, root_2))
