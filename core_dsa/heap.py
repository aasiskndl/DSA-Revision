# a heap is a complete binary tree that follows the heap property
# min heap: parent node <= its children (smallest element is always at the root)
# max heap: parent node >= its children  (largest element is always at the root)

# implementation of min heap
import heapq

heap = []

# insert the elements
heapq.heappush(heap, 20)
heapq.heappush(heap, 10)
heapq.heappush(heap, 30)
heapq.heappush(heap, 5)

print("Heap values: ", heap)

# peek (min element)
print("Min element: ", heap[0])

# delete (remove min)
print("Deleted element: ", heapq.heappop(heap))
print("Heap after deletion: ", heap)


# implementation of max heap
# python does not have direct max heap, we negate the values

max_heap = []
heapq.heappush(max_heap, -10)
heapq.heappush(max_heap, -40)
heapq.heappush(max_heap, -20)

print("Max element: ", -heapq.heappop(max_heap))
