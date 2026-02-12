"""
Docstring for dsa.core_dsa.prefix_sum
It is a technique where we build a new array that stores the cumulative (running) sum of elements from the begining of the array up to each position.
Instead of adding numbers again and again, we precompute totals once and reuse them later.

Time complexity: O(n)
"""


def build_prefix_sum(arr):
    prefix = [0] * len(arr)
    prefix[0] = arr[0]

    for i in range(1, len(arr)):
        prefix[i] = prefix[i - 1] + arr[i]
    return prefix


def range_sum(prefix, L, R):
    if L == 0:
        return prefix[R]
    return prefix[R] - prefix[L - 1]


arr = [2, 4, 1, 3, 6]
prefix = build_prefix_sum(arr)

print(range_sum(prefix, 1, 3))
