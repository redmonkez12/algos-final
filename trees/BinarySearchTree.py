class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return f'{self.val}'


class BSTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        # Prvne se zeptam, jestli existuje koren
        # Pokud ne, tak root bude novy uzel

        # V dalsim kroku budu porovnat jestli nove vlozena hodnota
        # je mensi nebo vetsi nez hodnota v predchozim uzlu
        # a budu to delat tak dlouho dokud nedojdu az na konec
        node = Node(val)

        if self.root is None:
            self.root = node
            return node

        current = self.root  # 8
        while True:
            if val < current.val:
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
    def search(self, val):
        if self.root is None:
            return None

        current = self.root

        while current:
            if val == current.val:
                return current
            if val < current.val:
                current = current.left
            else:
                current = current.right

        return None

    def delete(self, key):
        self.root = self.delete_node(self.root, key)

    def delete_node(self, root, key):
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
            # else:
            #     min_node = self.find_min(root.right)
            #     root.val = min_node.val
            #     root.right = self.delete_node(root.right, min_node.val)
            else:
                max_node = self.find_max(root.left)
                root.val = max_node.val
                root.left = self.delete_node(root.left, max_node.val)

        return root

    def find_min(self, node):
        while node.left is not None:
            node = node.left

        return node

    def find_max(self, node):
        while node.right is not None:
            node = node.right

        return node

    # def get_node_with_parent(self, data):
    #     parent = None
    #     current = self.root
    #
    #     if current is None:
    #         return parent, None  # parent - uzel, ktery se nazim najit current - nasledujici uzel
    #
    #     while current:
    #         if current.data == data:
    #             return parent, current
    #         elif current.data > data:  # jdu vlevo
    #             parent = current
    #             current = current.left
    #         else:  # jdu vpravo
    #             parent = current  # parent - 5
    #             current = current.right  # current - 9

        # return parent, current


    # def delete(self, data):
    #     # nemam zadny potomek - Vyreseno
    #     # mam jednoho potomka
    #     # mam dva potomky
    #     parent, node = self.get_node_with_parent(data)
    #     if parent is None and node is None:
    #         return False
    #
    #     if node.left and node.right:  # Uzel ma dva potomky
    #         parent_leftmost_node = node  # 3
    #         leftmost_node = node.right   # 5
    #         while leftmost_node.left:    # jestli ma nekoho vlevo
    #             parent_leftmost_node = leftmost_node  # 13
    #             leftmost_node = leftmost_node.left  # 12
    #         node.data = leftmost_node.data  # to je prohozeni
    #
    #         # print(parent_leftmost_node.data, leftmost_node.data)
    #         # V pripade to co jsem nasel, tak nema zadneho potomka
    #         if parent_leftmost_node.data == leftmost_node.data:  # 9 == 12
    #             parent_leftmost_node.left = leftmost_node.right  # None
    #         else:
    #             # protoze jdu co nejvic doleva, tak muze mit max jednoho potomka vpravo
    #             parent_leftmost_node.left = leftmost_node.right
    #
    #
    #     if node.left is None and node.right is None:
    #         if parent:  # jsem nekde pod korenem
    #             if parent.right is node:  # potrebuji z parenta smazat referenci na left nebo right
    #                 parent.right = None
    #             else:
    #                 parent.left = None
    #         else:  # je to koren - strom o jednom uzlu
    #             self.root = None
    #     else:
    #         next_node = None
    #         if node.left:
    #             next_node = node.left
    #         else:
    #             next_node = node.right
    #
    #         # uzel ma jednoho potomka
    #         if parent:
    #             if parent.left is node:  # aktualne parent.left 6
    #                 parent.left = next_node  # misto 6 davam 5
    #             else:
    #                 parent.right = next_node
    #         else:
    #             self.root = nodedef delete(self, data):
    #     # nemam zadny potomek - Vyreseno
    #     # mam jednoho potomka
    #     # mam dva potomky
    #     parent, node = self.get_node_with_parent(data)
    #     if parent is None and node is None:
    #         return False
    #
    #     if node.left and node.right:  # Uzel ma dva potomky
    #         parent_leftmost_node = node  # 3
    #         leftmost_node = node.right   # 5
    #         while leftmost_node.left:    # jestli ma nekoho vlevo
    #             parent_leftmost_node = leftmost_node  # 13
    #             leftmost_node = leftmost_node.left  # 12
    #         node.data = leftmost_node.data  # to je prohozeni
    #
    #         # print(parent_leftmost_node.data, leftmost_node.data)
    #         # V pripade to co jsem nasel, tak nema zadneho potomka
    #         if parent_leftmost_node.data == leftmost_node.data:  # 9 == 12
    #             parent_leftmost_node.left = leftmost_node.right  # None
    #         else:
    #             # protoze jdu co nejvic doleva, tak muze mit max jednoho potomka vpravo
    #             parent_leftmost_node.left = leftmost_node.right
    #
    #
    #     if node.left is None and node.right is None:
    #         if parent:  # jsem nekde pod korenem
    #             if parent.right is node:  # potrebuji z parenta smazat referenci na left nebo right
    #                 parent.right = None
    #             else:
    #                 parent.left = None
    #         else:  # je to koren - strom o jednom uzlu
    #             self.root = None
    #     else:
    #         next_node = None
    #         if node.left:
    #             next_node = node.left
    #         else:
    #             next_node = node.right
    #
    #         # uzel ma jednoho potomka
    #         if parent:
    #             if parent.left is node:  # aktualne parent.left 6
    #                 parent.left = next_node  # misto 6 davam 5
    #             else:
    #                 parent.right = next_node
    #         else:
    #             self.root = node



bst = BSTree()
bst.insert(17)
bst.insert(15)
bst.insert(50)
bst.insert(4)
bst.insert(16)
bst.insert(25)


# print(bst.root.left.right, "xxxxx")  # 5
# print(bst.root.right)
# bst.delete(3)
# print(bst.root.left, "yyy")
# bst.delete(3)
# print(bst.root.left, "xxxxx")  # 1
# bst.delete(1)
# bst.delete(10)
# print(bst.root.left.left, "Xxxxxxxxxx")
# print(bst.root.right, "yyyyyyyyy")

"""
      17
     /   \
    15     50
   /  \    /
  4    16 25
"""


# bst.delete(3)
# print("Pre order")

def pre_order(root):
    if root:
        print(root.val)
        pre_order(root.left)
        pre_order(root.right)

pre_order(bst.root)
bst.delete(15)
print(20 * "-")

pre_order(bst.root)

print("Pre order")
