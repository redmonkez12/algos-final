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
        self.head = None
        self.tail = None

    def _add_node(self, node):
        # Add a node to the front of the linked list
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def _remove_node(self, node):
        # Remove a node from the linked list
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        node.next = None
        node.prev = None

    def _move_to_head(self, node):
        # Move a node to the front of the linked list (most recently used)
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        # Remove and return the tail node (least recently used)
        tail_node = self.tail
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

    def print_cache(self):
        print("LRUCache:")
        current = self.head
        while current:
            print(f"Key: {current.key}, Value: {current.value}")
            current = current.next

cache = LRUCache(5)

cache.put("A", 1)
cache.put("B", 2)
cache.put("C", 3)

# cache.print_cache()
print(cache.get("A"))
# cache.print_cache()
print(cache.get("D"))
cache.put("E", 4)
cache.print_cache()

