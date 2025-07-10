"""
LeetCode 1553. Minimum Number of Days to Eat N Oranges

Given n oranges, return the minimum number of days to eat all oranges. You can eat 1, n/2, or n/3 oranges in a day.

Constraints:
- 1 <= n <= 2 * 10^9

Example:
Input: n = 10
Output: 4
"""
def minDays(n):
    from functools import lru_cache
    @lru_cache(None)
    def dp(x):
        if x <= 1:
            return x
        return 1 + min(x % 2 + dp(x // 2), x % 3 + dp(x // 3))
    return dp(n)

# Example usage:
n = 10
print(minDays(n))  # Output: 4
