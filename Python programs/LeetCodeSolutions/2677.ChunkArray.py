"""
LeetCode 2677. Chunk Array

Given arr and size, return the chunked array.

Constraints:
- 0 <= arr.length <= 10^5
"""

def chunk(arr, size):
    return [arr[i:i+size] for i in range(0, len(arr), size)]
# Example usage:
# print(chunk([1,2,3,4,5], 2))  # Output: [[1,2],[3,4],[5]]
