'''
Docstring for dsa.sorting_algos.quick
Quick sort is a highly efficient, comparision-based, divide and conquer sorting algorithm that sorts data in place 
by selecting a 'pivot' element, partitioning smaller elements to the left and larger elements to the right. 
It recursively sorts the sub-arrays, offering an average time complexity of O(n log n).

Worst case O(n^2): occours when the input array is alread sorted in the ascending or descending order.
            or, if the input sequence that consistently forces the pivot to be smallest or largest element in the curent sub-array.

'''

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)
        
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i+1], arr[high] = arr[high], arr[i + 1]
    return i+1

nums = [8,4,9,1,5,3]
quick_sort(nums, 0, len(nums) - 1)
print("Sorted array:", nums)
        
        
def quick_sort_verbose(arr, low, high, depth=0):
    indent = "  " * depth
    if low < high:
        pivot_index = partition_verbose(arr, low, high, depth)
        quick_sort_verbose(arr, low, pivot_index - 1, depth + 1)
        quick_sort_verbose(arr, pivot_index + 1, high, depth + 1)


def partition_verbose(arr, low, high, depth):
    indent = "  " * depth
    pivot = arr[high]
    print(f"{indent}Pivot chosen: {pivot} from {arr[low:high+1]}")
    
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            print(f"{indent} Swapped {arr[i]} and {arr[j]} → {arr}")
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print(f"{indent} Placed pivot → {arr}\n")
    return i + 1


nums = [8,4,9,1,5,3]
quick_sort_verbose(nums, 0, len(nums) - 1)
print("Final sorted:", nums)
