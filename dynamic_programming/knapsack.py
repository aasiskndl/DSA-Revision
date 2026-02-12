"""
Docstring for dynamic_programming.knapsack
You are given n items, each has its respective weights, values.
You have a knapsack that can carry capacity of W

Rule:
- you can either take an item or not to take it
- you cannot take the same item twice (that's why it is called 0/1)

Goal: is to maximize the total value without exceeding capacity.
"""


def knapsack(weights, values, W):
    n = len(weights)

    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
W = 7

print(knapsack(weights, values, W))
