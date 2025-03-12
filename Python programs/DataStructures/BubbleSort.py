

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to detect if any swap happens
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swap happens, array is already sorted
        if not swapped:
            break
    return arr

# Example usage
arr = [5, 3, 8, 4, 2]
print("Original array:", arr)
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)
