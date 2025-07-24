"""
LeetCode 2625. Flatten Deeply Nested Array

Given a nested list, return a flat list.

Constraints:
- 1 <= arr.length <= 10^5
"""

def flatten(arr):
    res = []
    for x in arr:
        if isinstance(x, list):
            res.extend(flatten(x))
        else:
            res.append(x)
    return res
# Example usage:
# print(flatten([1,[2,[3,4],5],6]))  # Output: [1,2,3,4,5,6]
