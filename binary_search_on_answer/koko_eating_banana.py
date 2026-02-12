"""
Docstring for core_dsa.koko_eating_banana
It is a classic problem for binary search where koko has piles of bananas.
She eats at speed k bananas/hr
goal is to return the minimum k so she can finish within h hrs
"""

import math


def min_eating_speed(piles, h):
    def can_finish(speed):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / speed)

        return hours <= h

    left = 1
    right = max(piles)
    answer = right

    while left <= right:
        mid = (left + right) // 2

        if can_finish(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer


piles = [3, 6, 7, 11]
h = 20
print("Minimum eating speed:", min_eating_speed(piles, h))
