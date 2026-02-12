"""
Docstring for dsa.sorting_algos.heap
Heap sort is an efficient, comparision-based, in-place sorting algorithm that uses a ninary heap data
structure to manage elements.
It works by transforming an us-sorted array into a max-heap(where parent nodes are larger than children),
repeatedly extracting the maximum element forom the root, and placing at the end of the array.

Time complexity: O(n log n)

"""


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # if left child is larger
    if left < n and arr[left] > arr[largest]:
        largest = left

    # if right child is larger
    if right < n and arr[right] > arr[largest]:
        largest = right

    # if root is not the largest, swap and continue heapify
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # build max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # extract elements one-by-one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


nums = [12, 11, 13, 8, 3, 1, 9]
heap_sort(nums)
print("sorted array:", nums)
