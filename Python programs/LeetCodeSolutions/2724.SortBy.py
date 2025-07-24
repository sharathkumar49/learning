"""
LeetCode 2724. Sort By

Implement a sort by function for a list.

Constraints:
- 0 <= arr.length <= 10^5
"""

def sortBy(arr, fn):
    return sorted(arr, key=fn)
# Example usage:
# print(sortBy([5,4,1,2,3], lambda x: x))  # Output: [1,2,3,4,5]
