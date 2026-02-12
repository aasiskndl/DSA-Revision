"""
Dynamic programming is the technique that solves a big problem by solving small problems one and then reusing them to solve a big problem

we can do it by:
- overlapping subproblems
- store results

"""


def fib(n):
    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


print(fib(6))
