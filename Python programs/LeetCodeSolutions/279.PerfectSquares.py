"""
279. Perfect Squares
https://leetcode.com/problems/perfect-squares/

Given an integer n, return the least number of perfect square numbers that sum to n.

Constraints:
- 1 <= n <= 10^4

Example 1:
Input: n = 12
Output: 3

Example 2:
Input: n = 13
Output: 2
"""
def numSquares(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1
    return dp[n]

# Example usage:
if __name__ == "__main__":
    print(numSquares(12))  # Output: 3
    print(numSquares(13))  # Output: 2
