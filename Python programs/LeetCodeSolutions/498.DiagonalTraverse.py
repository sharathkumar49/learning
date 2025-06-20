"""
498. Diagonal Traverse

Given an m x n matrix, return all elements of the matrix in diagonal order as described in the problem.

Constraints:
- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 10^4
- 1 <= m * n <= 10^4
- -10^5 <= mat[i][j] <= 10^5

Example:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
"""

class Solution:
    def findDiagonalOrder(self, mat: list) -> list:
        if not mat or not mat[0]:
            return []
        m, n = len(mat), len(mat[0])
        res = []
        for d in range(m + n - 1):
            intermediate = []
            r = 0 if d < n else d - n + 1
            c = d if d < n else n - 1
            while r < m and c > -1:
                intermediate.append(mat[r][c])
                r += 1
                c -= 1
            if d % 2 == 0:
                res.extend(intermediate[::-1])
            else:
                res.extend(intermediate)
        return res

# Example usage:
sol = Solution()
print(sol.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))  # Output: [1,2,4,7,5,3,6,8,9]
