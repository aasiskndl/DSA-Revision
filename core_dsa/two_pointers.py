"""
Docstring for dsa.core_dsa.two_pointers
Two-pointers technique is a DSA pattern that uses two indices to traverse linear data structures (arrays, strings or linked lists)
simultaneously, often reducing O(n^2) complexity to O(n).
It is primarily used for sorting/searching pairs, finding or reversing elements by moving pointers inward, outward or in the same direction.

Working: Instead of nested loops, two pointers move from start and end or both from start, adjusting based on conditions.
"""

# problem: find if there is a pair with sum = X.


def pair_with_sum(arr, target):
    # pointers
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return True
        elif current_sum < target:
            left = left + 1
        else:
            right -= 1
    return False


arr = [1, 2, 3, 4, 5, 6]
target = 6
print(pair_with_sum(arr, target))
