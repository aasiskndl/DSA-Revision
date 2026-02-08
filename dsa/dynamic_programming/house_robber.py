'''
Problem Statement:
You are a robber.
You have houses in a line, each with some money.
but here is the catch, you cannot rob two adjacent houses(alarm system)
goal is to maximize the money you can rob.
'''

def house_robber(nums):
    if not nums:
        return 0 
    if len(nums) == 1:
        return nums[0]
    
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i-2] + nums[i])
        
    return dp[-1]

houses = [2, 7, 9, 3, 1]
print(house_robber(houses))

