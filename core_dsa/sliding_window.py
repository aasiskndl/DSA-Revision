"""
Docstring for core_dsa.sliding_window
Sliding window is the type of problem in which you are given a sequence of arrays/strings and the goal is to find the longest
subset or patterns within contiguous data.
It uses two pointers (usually left and right) to define the boundar of the active window.

two types:
1. fixed size
2. variable size (dynamic)

It reduces time complexit from O(n^2) to O(n) by reusing results from the previous window calculation

"""


def len_of_longest_substring(s):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        # if duplicate character appears then srink window from left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

            # add current character
        char_set.add(s[right])

        # update the maxm length
        max_length = max(max_length, right - left + 1)

    return max_length


s = "abcabcbb"
result = len_of_longest_substring(s)

print("Length of longest substring without repeating characters:", result)
