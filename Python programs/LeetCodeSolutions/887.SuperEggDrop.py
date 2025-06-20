"""
887. Super Egg Drop

You are given k eggs and n floors. Return the minimum number of moves to find the critical floor.

Example 1:
Input: k = 1, n = 2
Output: 2

Example 2:
Input: k = 2, n = 6
Output: 3

Constraints:
- 1 <= k <= 100
- 1 <= n <= 10^4
"""
def superEggDrop(k, n):
    dp = [0] * (k+1)
    m = 0
    while dp[k] < n:
        m += 1
        for i in range(k, 0, -1):
            dp[i] = dp[i] + dp[i-1] + 1
    return m

# Example usage:
print(superEggDrop(1, 2))  # Output: 2
print(superEggDrop(2, 6))  # Output: 3
