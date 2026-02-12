"""
Docstring for dynamic_programming.climbing_stairs
Climbing stairs problem asks for the number of distinct ways to reach the top of a staircase with n steps, given that you can climb either 1 or 2 steps at a time.
It involves overlapping subproblems and optimal substructure.
"""


def climb_stairs(n):
    if n <= 1:
        return 1

    prev2 = 1
    prev1 = 1

    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr

    return prev1


print(climb_stairs(5))
