"""
LeetCode 764. Largest Plus Sign

You are given an integer n and a list of mines, where each mine is represented as [x, y].
Return the order of the largest axis-aligned plus sign of 1's contained in the grid with n x n size and mines.

Example 1:
Input: n = 5, mines = [[4,2]]
Output: 2

Example 2:
Input: n = 1, mines = [[0,0]]
Output: 0

Constraints:
- 1 <= n <= 500
- 0 <= mines.length <= 5000
- 0 <= mines[i][j] < n
"""
from typing import List

def orderOfLargestPlusSign(n: int, mines: List[List[int]]) -> int:
    banned = {tuple(m) for m in mines}
    dp = [[0]*n for _ in range(n)]
    for i in range(n):
        count = 0
        for j in range(n):
            count = 0 if (i, j) in banned else count + 1
            dp[i][j] = count
        count = 0
        for j in range(n-1, -1, -1):
            count = 0 if (i, j) in banned else count + 1
            dp[i][j] = min(dp[i][j], count)
    for j in range(n):
        count = 0
        for i in range(n):
            count = 0 if (i, j) in banned else count + 1
            dp[i][j] = min(dp[i][j], count)
        count = 0
        for i in range(n-1, -1, -1):
            count = 0 if (i, j) in banned else count + 1
            dp[i][j] = min(dp[i][j], count)
    return max(max(row) for row in dp)

# Example usage
if __name__ == "__main__":
    print(orderOfLargestPlusSign(5, [[4,2]]))  # Output: 2
    print(orderOfLargestPlusSign(1, [[0,0]]))  # Output: 0
