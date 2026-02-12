'''
Docstring for dsa.core_dsa.frequency_map
Frequency map stores how many times each element appears?
It helps to count things, detect duplicates, compare group of elements

Time complexity: O(n) 
'''

# for eg: to find if an array has any duplicates, we can use hashing approach
# in hashing technique, we store elements as we see them, if we see an element again then duplicate is found

def contains_duplicate(arr):
    seen ={}
    
    for num in arr:
        if num in seen:
            return True
        seen[num] = 1
        
    return False

arr= [1,2,6,4,8,1,5]
print(contains_duplicate(arr))