'''
Docstring for dsa.sorting_algos.selection
It organized a list by repeatedly finding the smallest element from the unsorted list.
Time complexity: O(n^2)
bhbj
'''

def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_index = i 
        
        for j in range(i+1, n):
            if arr[j]< arr[min_index]:
                min_index = j
                
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
    return arr

arr = [3,1,2,4,5]
print("Selection sort:", selection_sort(arr))
