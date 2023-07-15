class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def debug(self):
        curr = self.head
        out = ""

        for i in range(self.length):
            if curr is None:
                break

            out += f"{i} -> {curr.value} "
            curr = curr.next

        print(out)

    def prepend(self, value: str) -> None:
        node = Node(value)
        self.length += 1

        if self.head is None:
            self.head = node
            return

        node.next = self.head
        self.head.prev = node
        self.head = node

    def append(self, value: str) -> None:
        node = Node(value)
        self.length += 1

        if self.head is None:
            self.head = node
            return
        last = self.head
        while last.next:
            last = last.next

        last.next = node

    def remove(self, value: str) -> str | None:
        curr = self.head
        prev = None

        while curr:
            if curr.value == value:
                if prev is None:
                    self.head = curr.next
                else:
                    prev.next = curr.next
                break

            prev = curr
            curr = curr.next

        return curr.value

    def remove_at(self, index: int) -> str | None:
        if self.head is None:
            return

        temp = self.head

        if index == 0:
            self.head = temp.next
            temp = None
            return

        for i in range(index - 1):
            temp = temp.next
            if temp is None:
                break

        if temp is None:
            return

        if temp.next is None:
            return

        next_node = temp.next.next
        temp.next = None
        temp.next = next_node

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


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append("A")
    linked_list.append("B")
    linked_list.append("C")
    linked_list.append("D")
    linked_list.append("E")
    linked_list.append("F")
    linked_list.debug()
    linked_list.prepend("X")
    linked_list.remove("X")
    linked_list.debug()
    linked_list.remove_at(3)
    linked_list.debug()
