"""
768. Max Chunks To Make Sorted II

You are given an integer array arr. You can split the array into several "chunks" (subarrays), then sort each chunk individually and concatenate them to get the sorted array.
Return the maximum number of chunks you can make to sort the array.

Example 1:
Input: arr = [5,4,3,2,1]
Output: 1

Example 2:
Input: arr = [2,1,3,4,4]
Output: 4

Constraints:
- 1 <= arr.length <= 2000
- 0 <= arr[i] <= 10^8
"""
def maxChunksToSorted(arr):
    n = len(arr)
    max_left = [arr[0]] * n
    min_right = [arr[-1]] * n
    for i in range(1, n):
        max_left[i] = max(max_left[i-1], arr[i])
    for i in range(n-2, -1, -1):
        min_right[i] = min(min_right[i+1], arr[i])
    chunks = 1
    for i in range(n-1):
        if max_left[i] <= min_right[i+1]:
            chunks += 1
    return chunks

# Example usage:
print(maxChunksToSorted([5,4,3,2,1]))  # Output: 1
print(maxChunksToSorted([2,1,3,4,4]))  # Output: 4
