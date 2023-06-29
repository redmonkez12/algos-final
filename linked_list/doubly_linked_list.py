class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return f"{self.value}"


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def prepend(self, value: str) -> None:
        node = Node(value)
        self.length += 1

        if self.head is None:
            self.head = self.tail = node
            return

        node.next = self.head
        self.head.prev = node
        self.head = node

    def append(self, value: str) -> None:
        node = Node(value)
        self.length += 1

        if self.tail is None:
            self.head = self.tail = node
            return

        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    def remove(self, value: str) -> str | None:
        curr = self.head

        for i in range(0, self.length):
            if curr is None:
                break

            if curr.value == value:
                break

            curr = curr.next

        if curr is None:
            return

        return self.remove_node(curr)

    def remove_at(self, index: int) -> str | None:
        node = self.get_at(index)

        if node is None:
            return None

        return self.remove_node(node)

    def remove_node(self, node: Node) -> str | None:
        self.length = max(0, self.length - 1)

        if self.length == 0:
            out = self.head.value if self.head else None
            self.head = self.tail = None
            return out

        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

        if node == self.head:
            self.head = node.next

        if node == self.tail:
            self.tail = node.prev

        return node.value

    def get_at(self, index: int) -> None | Node:
        curr = self.head

        for i in range(0, index):
            if curr is None:
                break

            curr = curr.next

        return curr

    def debug(self):
        curr = self.head
        out = ""

        for i in range(self.length):
            if curr is None:
                break

            out += f"{i} -> {curr.value} "
            curr = curr.next

        print(out)


linked_list = DoublyLinkedList()
linked_list.append("A")
linked_list.append("B")
linked_list.append("C")
linked_list.append("D")
linked_list.append("E")
linked_list.append("F")
linked_list.debug()
linked_list.prepend("X")
linked_list.debug()
linked_list.remove_at(2)
linked_list.debug()
linked_list.remove("E")
linked_list.debug()
