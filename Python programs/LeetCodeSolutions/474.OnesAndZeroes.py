"""
474. Ones and Zeroes

Given an array of binary strings strs and two integers m and n, return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

Constraints:
- 1 <= strs.length <= 600
- 1 <= strs[i].length <= 100
- strs[i] consists only of '0' and '1'
- 1 <= m, n <= 100

Example:
Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
"""

class Solution:
    def findMaxForm(self, strs: list, m: int, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(m+1)]
        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')
            for i in range(m, zeros-1, -1):
                for j in range(n, ones-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones] + 1)
        return dp[m][n]

# Example usage:
sol = Solution()
print(sol.findMaxForm(["10","0001","111001","1","0"], 5, 3))  # Output: 4
