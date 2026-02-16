"""
generates the possible subsets from the list of numbers.
"""

def subsets(nums):
    result = []
    
    def backtrack(index, current):
        #  base case
        if index == len(nums):
            result.append(current[:])
            return 
        
        # choice 1: include nums[index]
        current.append(nums[index])
        backtrack(index + 1, current)
        
        # backtrack and undo the choice
        current.pop()
        
        # choice 2: exclude nums[index]
        backtrack(index + 1, current)
        
    backtrack(0, [])
    return result 

print(f"The subsets are\t", subsets([1,2,8,9]))

