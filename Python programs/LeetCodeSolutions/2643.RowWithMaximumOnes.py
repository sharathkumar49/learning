"""
LeetCode 2643. Row With Maximum Ones

Given a binary matrix, return the row with the maximum number of ones.

Constraints:
- 1 <= mat.length, mat[0].length <= 100
"""

def rowAndMaximumOnes(mat):
    return max([(sum(row), i) for i, row in enumerate(mat)])[1:]
# Example usage:
# print(rowAndMaximumOnes([[0,1],[1,0]]))  # Output: (1, 1)
