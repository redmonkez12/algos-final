from typing import Optional


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __repr__(self):
        return f"{self.value}"


class Bst:
    def __init__(self):
        self.root = None

    def insert(self, value: int) -> None:
        self.root = self._insert(self.root, value)

    def _insert(self, root: Optional[Node], value: int) -> Node:
        if root is None:
            return Node(value)

        if value < root.value:
            root.left = self._insert(root.left, value)
        else:
            root.right = self._insert(root.right, value)

        return root

    def depth_first_search(self, value: int) -> Node:
        return self._dfs(self.root, value)

    def _dfs(self, node: Optional[Node], value: int) -> Optional[Node]:
        if node is None:
            return node

        if node.value == value:
            return node

        left = self._dfs(node.left, value)
        if left:
            return left

        right = self._dfs(node.right, value)
        if right:
            return right

        return None

    def breadth_first_search(self, value: int) -> Optional[Node]:
        if self.root is None:
            return None

        stack = [self.root]

        while stack:
            current = stack.pop()

            if current.value == value:
                return current

            if current.right:
                stack.append(current.right)

            if current.left:
                stack.append(current.left)

        return None

    def delete_node(self, root: Optional[Node], key: int) -> Optional[Node]:
        if root is None:
            return None

        if key < root.val:
            root.left = self.delete_node(root.left, key)
        elif key > root.val:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                min_node = self.find_min(root.right)
                root.val = min_node.value
                root.right = self.delete_node(root.right, min_node.value)

        return root

    def find_min(self, node: Optional[Node]) -> Node:
        while node.left is not None:
            node = node.left

        return node

    def find_max(self, node: Optional[Node]) -> Node:
        while node.right is not None:
            node = node.right

        return node


bst = Bst()
bst.insert(8)
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(6)
bst.insert(14)
bst.insert(4)
bst.insert(7)
bst.insert(13)
print(bst.breadth_first_search(14))


# def pre_order(root):
#     if root:
#         print(root.value)
#         pre_order(root.left)
#         pre_order(root.right)
#
#
# pre_order(bst.root)


def breadth_first(root: Optional[Node]) -> None:
    if root is None:
        return None

    queue = [root]

    while queue:
        current = queue.pop(0)
        print(current.value)

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)


# breadth_first(bst.root)


# def depth_first(root: Optional[Node]) -> None:
#     if root is None:
#         return None
#
#     stack = [root]
#
#     while stack:
#         current = stack.pop()
#         print(current.value)
#
#         if current.right:
#             stack.append(current.right)
#
#         if current.left:
#             stack.append(current.left)


# def depth_first(root: Optional[Node]) -> None:
#     if root is None:
#         return None
#
#     print(root.value)
#     depth_first(root.left)
#     depth_first(root.right)
#
#
# depth_first(bst.root)

# The resulting BST:
#        8
#      /   \
#     3     10
#    / \      \
#   1   6      14
#      / \     /
#     4   7   13
