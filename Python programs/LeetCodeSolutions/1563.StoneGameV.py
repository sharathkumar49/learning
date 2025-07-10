"""
LeetCode 1563. Stone Game V

Given an array stoneValue, return the maximum score Alice can get by splitting the array as described in the problem statement.

Constraints:
- 1 <= stoneValue.length <= 500
- 1 <= stoneValue[i] <= 10^4

Example:
Input: stoneValue = [6,2,3,4,5,5]
Output: 18
"""
def stoneGameV(stoneValue):
    n = len(stoneValue)
    prefix = [0] * (n+1)
    for i in range(n):
        prefix[i+1] = prefix[i] + stoneValue[i]
    from functools import lru_cache
    @lru_cache(None)
    def dp(i, j):
        if i == j:
            return 0
        res = 0
        for k in range(i, j):
            left = prefix[k+1] - prefix[i]
            right = prefix[j+1] - prefix[k+1]
            if left < right:
                res = max(res, left + dp(i, k))
            elif left > right:
                res = max(res, right + dp(k+1, j))
            else:
                res = max(res, left + max(dp(i, k), dp(k+1, j)))
        return res
    return dp(0, n-1)

# Example usage:
stoneValue = [6,2,3,4,5,5]
print(stoneGameV(stoneValue))  # Output: 18
