"""
LeetCode 1764. Form Array by Concatenating Subarrays of Another Array

Given arrays arr and pieces, return true if arr can be formed by concatenating the arrays in pieces.

Example 1:
Input: arr = [85], pieces = [[85]]
Output: true

Constraints:
- 1 <= pieces.length <= arr.length <= 100
- sum(pieces[i].length) == arr.length
- 1 <= arr[i], pieces[i][j] <= 100
"""

def canFormArray(arr, pieces):
    d = {p[0]: p for p in pieces}
    res = []
    i = 0
    while i < len(arr):
        if arr[i] not in d:
            return False
        p = d[arr[i]]
        if arr[i:i+len(p)] != p:
            return False
        i += len(p)
    return True

# Example usage:
# arr = [85]
# pieces = [[85]]
# print(canFormArray(arr, pieces))  # Output: True
