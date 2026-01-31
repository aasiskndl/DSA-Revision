'''
Docstring for dsa.sorting_algos.insertion
The algorithm inerates through the unsorted part, repeatedly taking one element and inserting it into its correct position 
within the already sorted portion.
Time complexity: O(n) best case (if the array is already sorted)
                O(n^2) Worst case

'''

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -=1
            
        arr[j+1] = key
        
    return arr

nums = [8,3,5,1,9,5]
print("Expected result after sorting:", insertion_sort(nums.copy()))

