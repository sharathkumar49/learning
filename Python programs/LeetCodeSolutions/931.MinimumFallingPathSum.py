"""
931. Minimum Falling Path Sum
https://leetcode.com/problems/minimum-falling-path-sum/

Given an n x n integer matrix matrix, return the minimum sum of any falling path through matrix.
A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. The path continues until it reaches the last row.

Constraints:
- n == matrix.length == matrix[i].length
- 1 <= n <= 100
- -100 <= matrix[i][j] <= 100

Example:
Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
"""
from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for i in range(1, n):
            for j in range(n):
                matrix[i][j] += min(
                    matrix[i-1][j],
                    matrix[i-1][j-1] if j > 0 else float('inf'),
                    matrix[i-1][j+1] if j < n-1 else float('inf')
                )
        return min(matrix[-1])

# Example usage
if __name__ == "__main__":
    matrix = [[2,1,3],[6,5,4],[7,8,9]]
    print(Solution().minFallingPathSum(matrix))  # Output: 13
