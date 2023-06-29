class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f'{self.data}'


class BSTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # Prvne se zeptam, jestli existuje koren
        # Pokud ne, tak root bude novy uzel

        # V dalsim kroku budu porovnat jestli nove vlozena hodnota
        # je mensi nebo vetsi nez hodnota v predchozim uzlu
        # a budu to delat tak dlouho dokud nedojdu az na konec
        node = Node(data)

        if self.root is None:
            self.root = node
            return node

        current = self.root  # 8
        while True:
            parent = current
            if node.data < parent.data:  # 3 < 8
                # pujdu doleva
                current = current.left  # current = None, tady jsme prisli o referenci na puvodni uzel
                if current is None:
                    parent.left = node  # None.left = node
                    return node
            else:
                current = current.right
                # pujdu do prava
                if current is None:
                    parent.right = node
                    return node


    def get_node_with_parent(self, data):
        parent = None
        current = self.root

        if current is None:
            return parent, None  # parent - uzel, ktery se nazim najit current - nasledujici uzel

        while current:
            if current.data == data:
                return parent, current
            elif current.data > data:  # jdu vlevo
                parent = current
                current = current.left
            else:  # jdu vpravo
                parent = current  # parent - 5
                current = current.right  # current - 9

        return parent, current


    def delete(self, data):
        # nemam zadny potomek - Vyreseno
        # mam jednoho potomka
        # mam dva potomky
        parent, node = self.get_node_with_parent(data)
        if parent is None and node is None:
            return False

        if node.left and node.right:  # Uzel ma dva potomky
            parent_leftmost_node = node  # 3
            leftmost_node = node.right   # 5
            while leftmost_node.left:    # jestli ma nekoho vlevo
                parent_leftmost_node = leftmost_node  # 13
                leftmost_node = leftmost_node.left  # 12
            node.data = leftmost_node.data  # to je prohozeni

            # print(parent_leftmost_node.data, leftmost_node.data)
            # V pripade to co jsem nasel, tak nema zadneho potomka
            if parent_leftmost_node.data == leftmost_node.data:  # 9 == 12
                parent_leftmost_node.left = leftmost_node.right  # None
            else:
                # protoze jdu co nejvic doleva, tak muze mit max jednoho potomka vpravo
                parent_leftmost_node.left = leftmost_node.right


        if node.left is None and node.right is None:
            if parent:  # jsem nekde pod korenem
                if parent.right is node:  # potrebuji z parenta smazat referenci na left nebo right
                    parent.right = None
                else:
                    parent.left = None
            else:  # je to koren - strom o jednom uzlu
                self.root = None
        else:
            next_node = None
            if node.left:
                next_node = node.left
            else:
                next_node = node.right

            # uzel ma jednoho potomka
            if parent:
                if parent.left is node:  # aktualne parent.left 6
                    parent.left = next_node  # misto 6 davam 5
                else:
                    parent.right = next_node
            else:
                self.root = node



bst = BSTree()
print(bst.root)
bst.insert(8)
bst.insert(10)
print(bst.root)
bst.insert(3)
bst.insert(5)
bst.insert(1)


print(bst.root.left.right, "xxxxx")  # 5
print(bst.root.right)
# bst.delete(3)
print(bst.root.left, "yyy")
# bst.delete(3)
# print(bst.root.left, "xxxxx")  # 1
# bst.delete(1)
# bst.delete(10)
# print(bst.root.left.left, "Xxxxxxxxxx")
# print(bst.root.right, "yyyyyyyyy")

"""
      8
     / \
    3   10
   /  \
  1    5
"""


bst.delete(3)
print("Pre order")

def pre_order(root):
    if root:
        print(root.data)
        pre_order(root.left)
        pre_order(root.right)

pre_order(bst.root)

print("Pre order")
