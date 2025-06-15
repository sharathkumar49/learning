# A#pproach 1: K-Way Merge Using Min-Heap
# You can merge multiple sorted arrays efficiently using the 
# k-way merge technique, leveraging a min-heap (priority queue).
# Since you want to avoid default sorting modules, we’ll implement
# a heap manually using an array and maintain it with heapify operations.

# Here's a Python program to merge more than two sorted arrays
# without relying on built-in sorting functions:

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, value, array_index, element_index):
        self.heap.append((value, array_index, element_index))
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index][0] < self.heap[parent][0]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index):
        size = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index
            if left < size and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left
            if right < size and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right
            if smallest == index:
                break
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest

    def is_empty(self):
        return len(self.heap) == 0

def merge_sorted_arrays(arrays):
    min_heap = MinHeap()
    result = []

    # Insert first elements of each array into heap
    for i, arr in enumerate(arrays):
        if arr:  # Ensure array is not empty
            min_heap.push(arr[0], i, 0)

    while not min_heap.is_empty():
        value, array_index, element_index = min_heap.pop()
        result.append(value)

        # If there's a next element in the same array, insert it
        if element_index + 1 < len(arrays[array_index]):
            min_heap.push(arrays[array_index][element_index + 1], array_index, element_index + 1)

    return result

# Example usage
arrays = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [0, 10, 11]
]

merged_array = merge_sorted_arrays(arrays)
print("Merged Sorted Array:", merged_array)

# Explanation:
# A MinHeap stores the smallest element among all arrays.
# We push the first element of each sorted array into the heap.
# We pop the smallest element, add it to the result, and push the next element from the same array.
# This continues until all elements are merged.

# This achieves O(N log K) complexity, where N is the total number of elements,
# and K is the number of arrays. 







# Approach 2: Iterative Two-Way Merge (Pairwise Merging)
# Iterative Two-Way Merge (Pairwise Merging):
# Instead of using a heap, we merge arrays two at a time.
# This follows a divide-and-conquer strategy similar to merging in Merge Sort.

def merge_two_sorted_arrays(arr1, arr2):
    i, j = 0, 0
    merged = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    
    # Append remaining elements
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    
    return merged

def merge_multiple_sorted_arrays(arrays):
    while len(arrays) > 1:
        merged_arrays = []
        
        # Merge pairs of arrays
        for i in range(0, len(arrays) - 1, 2):
            merged_arrays.append(merge_two_sorted_arrays(arrays[i], arrays[i + 1]))
        
        # If an odd number of arrays, add the last one unmerged
        if len(arrays) % 2 == 1:
            merged_arrays.append(arrays[-1])
        
        arrays = merged_arrays
    
    return arrays[0] if arrays else []

# Example usage
arrays = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [0, 10, 11]
]

merged_array = merge_multiple_sorted_arrays(arrays)
print("Merged Sorted Array:", merged_array)

# Complexity: O(N log K), 
# where N is the total number of elements, and K is the number of arrays.

# Code Explanation:
# This program merges multiple sorted arrays using a 
# pairwise iterative merging strategy. 
# It follows a divide-and-conquer approach like Merge Sort,
# but instead of using a heap, it merges arrays two at a time.

# Step 1: Function to Merge Two Sorted Arrays
# The helper function merge_two_sorted_arrays(arr1, arr2) merges two sorted arrays into one sorted array.

# Example:
# merge_two_sorted_arrays([1, 4, 7], [2, 5, 8]) 
# Output: [1, 2, 4, 5, 7, 8]

# Step 2: Function to Merge Multiple Sorted Arrays
# The merge_multiple_sorted_arrays(arrays) function merges multiple sorted arrays iteratively by merging pairs of arrays at each step.

# How It Works:
# Iteratively merges arrays two at a time until only one fully merged array remains.
# If there is an odd number of arrays, the last one is carried forward unmerged to the next iteration.




# Approach 3: Modified Merge Sort Approach
# Modified Merge Sort Approach:
# This method recursively merges arrays, similar to a binary merge process.
# It ensures balanced merging and is more efficient than straightforward
# pairwise merging.

def merge_sorted_arrays_recursive(arrays, left, right):
    if left == right:
        return arrays[left]

    if right - left == 1:
        return merge_two_sorted_arrays(arrays[left], arrays[right])

    mid = (left + right) // 2
    left_merged = merge_sorted_arrays_recursive(arrays, left, mid)
    right_merged = merge_sorted_arrays_recursive(arrays, mid + 1, right)

    return merge_two_sorted_arrays(left_merged, right_merged)

def merge_k_sorted_arrays(arrays):
    if not arrays:
        return []
    return merge_sorted_arrays_recursive(arrays, 0, len(arrays) - 1)

# Example usage
arrays = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [0, 10, 11]
]

merged_array = merge_k_sorted_arrays(arrays)
print("Merged Sorted Array:", merged_array)


# Complexity: O(N log K), due to the recursive merging structure.

# Each method has its advantages:
# Heap-based k-way merging: Optimal for K being large.
# Pairwise merging: Simple and effective when K is small.
# Recursive divide-and-conquer merging: Well-balanced for cases where arrays
# have similar sizes.
