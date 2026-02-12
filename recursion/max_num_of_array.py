def find_max(arr, n):
    if n == 1:
        return arr[0]
    return max(arr[n - 1], find_max(arr, n - 1))


arr = [3, 7, 2, 9, 5]
print(find_max(arr, len(arr)))
