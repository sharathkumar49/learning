"""
769. Max Chunks To Make Sorted

You are given an array arr that is a permutation of [0, 1, ..., arr.length - 1].
We split the array into some number of "chunks" (subarrays), and individually sort each chunk. After concatenating them, the result is the sorted array.
Return the maximum number of chunks we can make to sort the array.

Example 1:
Input: arr = [4,3,2,1,0]
Output: 1

Example 2:
Input: arr = [1,0,2,3,4]
Output: 4

Constraints:
- 1 <= arr.length <= 10^4
- 0 <= arr[i] < arr.length
- All the elements of arr are unique.
"""
def maxChunksToSorted(arr):
    max_so_far = 0
    chunks = 0
    for i, num in enumerate(arr):
        max_so_far = max(max_so_far, num)
        if max_so_far == i:
            chunks += 1
    return chunks

# Example usage:
print(maxChunksToSorted([4,3,2,1,0]))  # Output: 1
print(maxChunksToSorted([1,0,2,3,4]))  # Output: 4
