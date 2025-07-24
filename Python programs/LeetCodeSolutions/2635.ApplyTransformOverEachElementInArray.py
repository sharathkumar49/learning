"""
LeetCode 2635. Apply Transform Over Each Element in Array

Implement a map function for a list.

Constraints:
- 0 <= arr.length <= 10^5
"""

def mapArray(arr, fn):
    return [fn(x) for x in arr]
# Example usage:
# print(mapArray([1,2,3], lambda x: x+1))  # Output: [2, 3, 4]
