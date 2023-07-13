import heapq

heap = []

nums = [5, 2, 3, 6, 8, 7, 1]

for num in nums:
    heapq.heappush(heap, num)

print(heap)
heapq.heappop(heap)
print(heap)
heapq.heappop(heap)
print(heap)
