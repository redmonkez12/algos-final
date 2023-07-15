from linked_list.singly_linked_list import LinkedList


class Node:
    def __init__(self, value):
        self.value = value
        self.next = next


def reverse_list(head):
    prev = None
    curr = head

    while curr:
        nxt = curr.next  # C
        curr.next = prev  # A
        prev = curr  # A
        curr = nxt  # B

    return prev

# 1. A -> None
# 2. B -> A -> None


linked_list = LinkedList()

values = ["A", "B", "C", "D", "E"]
for value in values:
    linked_list.append(value)

linked_list.debug()
linked_list.head = reverse_list(linked_list.head)
linked_list.debug()

