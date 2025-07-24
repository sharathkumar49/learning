"""
LeetCode 2634. Filter Elements from Array

Implement a filter function for a list.

Constraints:
- 0 <= arr.length <= 10^5
"""

def filterArray(arr, fn):
    return [x for x in arr if fn(x)]
# Example usage:
# print(filterArray([0,10,20,30], lambda x: x > 10))  # Output: [20, 30]
