'''
Docstring for dsa.sorting_algos.bubble
Repeatedly swap adjacent elements if they are in wrong order.
Largest elements "Jumps" to the end. This sequence follows until the whole array is sorted.
Time complexity: O(n^2)
'''

def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False   # checks if the list is already sorted or not
        
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                
        if not swapped:
            break 
    return arr

nums = [5,1,4,2,8]
print("Bubble sort:", bubble_sort(nums.copy()))