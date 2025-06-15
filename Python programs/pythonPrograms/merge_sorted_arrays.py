

def merge_sorted_arrays(arr1, arr2):
    merged = []
    i, j = 0, 0

    # Merge the arrays using two pointers
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    # Append remaining elements from arr1
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    # Append remaining elements from arr2
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged

# Example usage
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
merged_array = merge_sorted_arrays(arr1, arr2)
print("Merged Sorted Array:", merged_array)

# Explanation:
# The program initializes two pointers, i and j, to track elements in arr1 and arr2.
# It compares elements and appends the smaller one to the result merged list.
# Any remaining elements in either array are appended after the main merging process.
# This approach runs in O(n + m) time complexity, where n and m are the lengths of the input arrays—making it efficient compared to concatenating and sorting.






# In-Place Merge of Two Sorted Arrays
# If the two sorted arrays are stored consecutively in memory (like in a single list), we can merge them in-place without using extra space. Here’s how:


def merge_in_place(arr1, arr2):
    i = len(arr1) - 1  # Last index of arr1
    j = len(arr2) - 1  # Last index of arr2
    k = len(arr1) + len(arr2) - 1  # Last index of merged array

    # Expand arr1 to accommodate merged values
    arr1.extend([None] * len(arr2))

    # Merge from the end to prevent overwriting useful data
    while j >= 0:
        if i >= 0 and arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            i -= 1
        else:
            arr1[k] = arr2[j]
            j -= 1
        k -= 1

    return arr1

# Example usage
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
merged_array = merge_in_place(arr1, arr2)
print("Merged Sorted Array (In-Place):", merged_array)


# How It Works
# Extend arr1 to fit the elements from arr2.
# Use three pointers (i, j, k), starting from the end.
# Merge backwards to avoid overwriting elements in arr1.
# Time complexity: O(n + m), since each element is processed once.
# Space complexity: O(1) (in-place).




# In-Place Sorting vs. Normal Sorting in Merge Operations
# When merging sorted arrays, the distinction between 
# in-place sorting and normal sorting primarily concerns 
# space complexity and memory usage.

# 1. Normal Sorting (Using Extra Space):
# Typically involves creating a new array to store the merged result.
# Uses auxiliary space proportional to the number of elements.

# Example: The traditional two-pointer merge algorithm stores the merged result in a separate list.

# def merge_sorted_arrays(arr1, arr2):
#     merged = []
#     i, j = 0, 0

#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] < arr2[j]:
#             merged.append(arr1[i])
#             i += 1
#         else:
#             merged.append(arr2[j])
#             j += 1

#     merged.extend(arr1[i:])
#     merged.extend(arr2[j:])

#     return merged

# Space Complexity: O(n + m) (since it creates a new merged list) 
# Time Complexity: O(n + m) (since each element is processed once)



# 2. In-Place Sorting (Without Extra Space)
# Avoids creating a new array, directly modifies one of the input arrays.
# Requires careful index manipulation to merge efficiently.
# Typically involves shifting elements to make space while merging.

# Example: Merging two sorted arrays in-place, assuming arr1 has enough space at the end to accommodate arr2.

# def merge_in_place(arr1, arr2):
#     i = len(arr1) - 1
#     j = len(arr2) - 1
#     k = len(arr1) + len(arr2) - 1

#     arr1.extend([None] * len(arr2))

#     while j >= 0:
#         if i >= 0 and arr1[i] > arr2[j]:
#             arr1[k] = arr1[i]
#             i -= 1
#         else:
#             arr1[k] = arr2[j]
#             j -= 1
#         k -= 1

#     return arr1

# Space Complexity: O(1) (no extra space used) 
# Time Complexity: O(n + m)

# Key Differences
# Feature	         Normal Sorting (Extra Space)	         In-Place Sorting
# Space Used	     O(n + m) (new list)	                O(1) (direct modification)
# Time Complexity	 O(n + m)	                            O(n + m)
# Data Movement	     Elements copied to new list	        Elements shifted within the same array
# Suitability	     Useful when preserving input arrays	Best when modifying an existing array