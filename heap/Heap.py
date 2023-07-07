class MinHeap:
    pass
class MinHeap:
    def __init__(self):
        self.heap = []

    def get_parent(self, i):
        return (i - 1) // 2

    # def insert(self, data):
    #     self.heap.append(data)
    #     self.heapify_up(len(self.heap) - 1)

    def insert(self, data):
        self.heap.append(data)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self.get_parent(i)]:
            parent = self.get_parent(i)
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent

    def get_left_child(self, i):
        return 2 * i + 1

    def get_right_child(self, i):
        return 2 * i + 2

    def remove_first(self):
        if len(self.heap) == 0:
            return None

        min_value = self.heap[0]
        last_value = self.heap.pop()

        if len(self.heap) > 0:
            self.heap[0] = last_value
            self.heapify_down(0)

        return min_value

    def heapify_down(self, i):
        size = len(self.heap)
        smallest = i
        left_child = self.get_left_child(i)
        right_child = self.get_right_child(i)

        if left_child < size and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child

        if right_child < size and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify_down(smallest)

    def preorder_traversal(self):
        if not self.heap:
            return []

        result = []
        self._preorder(0, result)
        return result

    def _preorder(self, index, result):
        if index >= len(self.heap):
            return

        result.append(self.heap[index])  # Process current node
        self._preorder(2 * index + 1, result)  # Recurse on left child
        self._preorder(2 * index + 2, result)

heap = MinHeap()

# Insert elements into the heap
heap.insert(5)
heap.insert(3)
heap.insert(8)
heap.insert(2)
heap.insert(10)
# result = heap.preorder_traversal()
# print(result)
print(heap.heap)

heap.insert(1)
# print(value)
print(heap.heap)

# result = heap.preorder_traversal()
# print(result)