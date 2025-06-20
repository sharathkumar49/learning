"""
808. Soup Servings

There are two types of soup in A and B. Each time you serve, you can choose one of four operations. Return the probability that soup A will be empty first, plus half the probability that both A and B become empty at the same time.

Example 1:
Input: n = 50
Output: 0.62500

Example 2:
Input: n = 100
Output: 0.71875

Constraints:
- 0 <= n <= 10^9
- Answers within 10^-6 of the true value will be accepted.
"""
def soupServings(n):
    if n > 4800:
        return 1.0
    from functools import lru_cache
    @lru_cache(None)
    def dp(a, b):
        if a <= 0 and b <= 0:
            return 0.5
        if a <= 0:
            return 1
        if b <= 0:
            return 0
        return 0.25 * (dp(a-100, b) + dp(a-75, b-25) + dp(a-50, b-50) + dp(a-25, b-75))
    return dp(n, n)

# Example usage:
print(f"{soupServings(50):.5f}")   # Output: 0.62500
print(f"{soupServings(100):.5f}")  # Output: 0.71875
