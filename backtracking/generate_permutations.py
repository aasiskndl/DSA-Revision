"""
from the given list of numbers, return all possible orderings.
"""

def permute(nums):
    result = []
    used = [False] * len(nums)
    
    def backtrack(current):
        if len(current) == len(nums):
            result.append(current[:])
            return 
        
        for i in range(len(nums)):
            if used[i]:
                continue
            
            #choose
            used[i] = True
            current.append(nums[i])
            
            # explore
            backtrack(current)
            
            # backtrack
            current.pop()
            used[i] = False
            
    backtrack([])
    return result
    
print(f"All the possible orderings are:\n",permute([1,2,3]))