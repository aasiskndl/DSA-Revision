def subsets(nums):
    result = []
    
    def backtrack(index, current):
        # Base case: reached end
        if index == len(nums):
            result.append(current[:])  # copy
            return
        
        # Choice 1: include nums[index]
        current.append(nums[index])
        backtrack(index + 1, current)
        
        # Backtrack (undo the choice)
        current.pop()
        
        # Choice 2: exclude nums[index]
        backtrack(index + 1, current)
    
    backtrack(0, [])
    return result


print(subsets([1, 2]))
