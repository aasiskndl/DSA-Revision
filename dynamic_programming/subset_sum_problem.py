'''
Docstring for dynamic_programming.subset_sum_problem
You are given a list of positive integers (numbers) and a target value (target)

goal is to determine if there exists a subset of numbers whose sum equals to the target value
we only return true or false
'''

def subset_sum(nums, target):
    n = len(nums)
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    
    # base case: sum 0 is always possible
    for i in range(n+1):
        dp[i][0] = True
        
    for i in range(1, n+1):
        for s in range(1, target+1):
            if nums[i-1]>s:
                dp[i][s] = dp[i-1][s]
            else:
                dp[i][s] = dp[i-1][s] or dp[i-1][s-nums[i-1]]
                
    return dp[n][target]
    
nums = [3,34,4,12,5,2]
target = 9
print(subset_sum(nums, target))