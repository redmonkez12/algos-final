class MinHeap:
    def __init__(self):
        self.heap = []

    def get_parent(self, i):
        return (i - 1) // 2

    def insert(self, data):
        self.heap.append(data)
        self.heapify_up(len(self.heap) - 1)

    def remove_first(self):
        if len(self.heap) == 0:
            return None

        min_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heapify_down(0)

        return min_value

    def heapify_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self.get_parent(i)]:
            # parent_id = self.get_parent(i)

            self.heap[i], self.heap[self.get_parent(i)] = self.heap[self.get_parent(i)], self.heap[i]
            i = self.get_parent(i)

    def heapify_down(self, i):
        left_child = 2 * 1 + 1
        right_child = 2 * 1 + 2
        smallest = i

        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child

        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]  # 71, 201
            self.heapify_down(smallest)

