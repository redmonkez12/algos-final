class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        # Add a node to the front of the linked list
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        # Remove a node from the linked list
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_head(self, node):
        # Move a node to the front of the linked list (most recently used)
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        # Remove and return the tail node (least recently used)
        tail_node = self.tail.prev
        self._remove_node(tail_node)
        return tail_node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._move_to_head(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            if len(self.cache) == self.capacity:
                tail_node = self._pop_tail()
                del self.cache[tail_node.key]

            new_node = ListNode(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)
