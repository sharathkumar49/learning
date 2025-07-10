"""
LeetCode 1640. Check Array Formation Through Concatenation

Given an array arr and a 2D array pieces, return true if arr can be formed by concatenating the arrays in pieces in any order.

Example 1:
Input: arr = [85], pieces = [[85]]
Output: true

Constraints:
- 1 <= pieces.length <= arr.length <= 100
- 1 <= pieces[i].length <= 100
- 1 <= arr[i], pieces[i][j] <= 100
"""

def canFormArray(arr, pieces):
    d = {p[0]: p for p in pieces}
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
