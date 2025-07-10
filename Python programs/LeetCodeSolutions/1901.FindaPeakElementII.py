"""
LeetCode 1901. Find a Peak Element II

Given a 2D matrix, find a peak element (greater than its neighbors). Return the coordinates of any peak.

Example:
Input: mat = [[1,4],[3,2]]
Output: [0,1]

Constraints:
- 1 <= mat.length, mat[i].length <= 500
- 1 <= mat[i][j] <= 10^5
"""

def findPeakGrid(mat):
    m, n = len(mat), len(mat[0])
    left, right = 0, n-1
    while left <= right:
        mid = (left + right) // 2
        max_row = max(range(m), key=lambda x: mat[x][mid])
        if mid > 0 and mat[max_row][mid] < mat[max_row][mid-1]:
            right = mid - 1
        elif mid < n-1 and mat[max_row][mid] < mat[max_row][mid+1]:
            left = mid + 1
        else:
            return [max_row, mid]

# Example usage:
# print(findPeakGrid([[1,4],[3,2]]))  # Output: [0,1]
