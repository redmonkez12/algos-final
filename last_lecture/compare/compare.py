class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.value}"


"""
    Root - 7


        7
       / \
     23    8
    / \   / \
   5  4  21 15
"""


def compare(a, b):
    # spravnou sktukturu
    # hodnoty
    # rekurze

    # strukturalni kontrola
    if a is None and b is None:
        return True

    # strukturalni kontrola
    if a is None or b is None:  # jedna hodnota musi byt not None protoze radek 27 to vylouci
        return False

    if a.value != b.value:
        return False

    # B.left = None B.left = C
    return compare(a.left, b.left) and compare(a.right, b.right)
    # 1 1
    # 1 0
    # 0 1


root_1 = Node("A")
root_1.left = Node("B")
root_1.right = Node("C")

root_2 = Node("A")
root_2.left = Node("B")
root_2.left.left = Node("C")


# root_1 = Node(7)
# root_1.left = Node(23)
# root_1.right = Node(8)
# root_1.left.left = Node(5)
# root_1.left.right = Node(4)
# root_1.right.left = Node(21)
# root_1.right.right = Node(15)
#
#
# root_2 = Node(7)
# root_2.left = Node(23)
# root_2.right = Node(8)
# root_2.left.left = Node(5)
# root_2.left.right = Node(4)
# root_2.right.left = Node(21)
# root_2.right.right = Node(15)

result = compare(root_1, root_2)
print(result)
