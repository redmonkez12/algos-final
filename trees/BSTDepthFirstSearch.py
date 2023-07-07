from typing import Optional


class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.value}"


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value: int) -> Node:
        node = Node(value)

        if self.root is None:
            self.root = node
            return node

        current = self.root

        while True:
            if value < current.value:
                if current.left is None:
                    current.left = node
                    return node
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = node
                    return node
                else:
                    current = current.right

    # def find(self, value: int) -> Optional[None]:
    #     if self.root is None:
    #         return None
    #
    #     stack = [self.root]
    #
    #     while stack:
    #         node = stack.pop()
    #
    #         if node.value == value:
    #             return node
    #         if node.right:
    #             stack.append(node.right)
    #         if node.left:
    #             stack.append(node.left)
    #
    #     return None

    def find(self, value: int) -> Optional[Node]:
        return self._dfs_find_recursive(self.root, value)

    def _dfs_find_recursive(self, node: Optional[Node], value: int) -> Optional[Node]:
        if node is None or node.value == value:
            return node

        if value < node.value:
            return self._dfs_find_recursive(node.left, value)
        else:
            return self._dfs_find_recursive(node.right, value)


bst = BST()
values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
for value in values:
    bst.insert(value)

print(bst.find(6))
