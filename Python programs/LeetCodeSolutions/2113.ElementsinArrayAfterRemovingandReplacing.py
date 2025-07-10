"""
LeetCode 2113. Elements in Array After Removing and Replacing

Given an array arr, remove and replace elements as described, and return the resulting array.

Example:
Input: arr = [1,2,3,4,5], remove = [2,4], replace = [6,7]
Output: [1,3,5,6,7]

Constraints:
- 1 <= arr.length <= 1000
- 1 <= remove.length, replace.length <= 100
"""

def removeAndReplace(arr, remove, replace):
    s = set(remove)
    res = [x for x in arr if x not in s]
    res.extend(replace)
    return res

# Example usage:
# print(removeAndReplace([1,2,3,4,5], [2,4], [6,7]))  # Output: [1,3,5,6,7]
