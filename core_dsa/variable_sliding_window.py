"""
Docstring for dsa.core_dsa.variable_sliding_window
Variable sliding window is the problem used to find an optimal contigious subarray or substring by dynamically adjusting the window size
based on specific constraints, rather than using a fixed size.

left pointer -> at the start of window
right pointer -> end of window

TIme complexity: it optimized O(n^2) problem to O(n) by expanding the right pointer to include elements and shrinking the left pointer when conditions are violated

"""


def length_of_longest_substring(s):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):

        # if duplicate, shrink window
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        # add current character
        char_set.add(s[right])

        # update max window size
        max_length = max(max_length, right - left + 1)

    return max_length


print(length_of_longest_substring("pwwdeew"))
