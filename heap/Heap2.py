class MinHeap:
    def __init__(self):
        self.heap = []

    def get_parent(self, i):
        return (i - 1) // 2

    def get_left_child(self, i):
        return 2 * i + 1

    def get_right_child(self, i):
        return 2 * i + 2

    def insert(self, data):
        self.heap.append(data)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, i):
        # while i > 0 and self.heap[i] < self.heap[self.get_parent(i)]:
        #     parent = self.get_parent(i)
        #     self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
        #     i = parent
        p = self.get_parent(i)
        parent_value = self.heap[p]
        value = self.heap[i]

        if parent_value < value:
            self.heap[i] = parent_value
            self.heap[p] = parent_value
            self.heapify_up(p)


    def remove_min(self):
        if not self.heap:
            return None

        min_value = self.heap[0]
        last_element = self.heap.pop()

        if self.heap:
            self.heap[0] = last_element
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
heap = MinHeap()

# Insert elements into the heap
heap.insert(5)
heap.insert(3)
heap.insert(8)
heap.insert(2)
heap.insert(10)
heap.insert(1)

# Remove the minimum element
# min_value = heap.remove_min()
# print("Minimum value:", min_value)

# Print the current heap
print("Current heap:", heap.heap)
