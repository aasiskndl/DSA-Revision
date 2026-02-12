def is_palindrome(s, left, right):
    # Base case
    if left >= right:
        return True

    # If mismatch
    if s[left] != s[right]:
        return False

    # Recursive call on smaller substring
    return is_palindrome(s, left + 1, right - 1)


s = "racecar"
print(is_palindrome(s, 0, len(s) - 1))  # True
