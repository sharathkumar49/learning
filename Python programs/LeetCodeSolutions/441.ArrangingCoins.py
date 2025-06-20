"""
441. Arranging Coins

You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the i-th row has exactly i coins. The last row of the staircase may be incomplete.
Given the integer n, return the number of complete rows of the staircase you will build.

Constraints:
- 0 <= n <= 2^31 - 1

Example:
Input: n = 5
Output: 2
"""

class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            mid = (left + right) // 2
            if mid * (mid + 1) // 2 <= n:
                left = mid + 1
            else:
                right = mid - 1
        return right

# Example usage:
sol = Solution()
print(sol.arrangeCoins(5))  # Output: 2
