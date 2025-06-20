"""
837. New 21 Game

Alice starts with 0 points and draws numbers from 1 to maxPts with equal probability. She stops drawing when she reaches k or more points. Return the probability that she has n or fewer points.

Example 1:
Input: n = 10, k = 1, maxPts = 10
Output: 1.0

Example 2:
Input: n = 6, k = 1, maxPts = 10
Output: 0.6

Constraints:
- 0 <= k <= n <= 10^4
- 1 <= maxPts <= 10^4
"""
def new21Game(n, k, maxPts):
    if k == 0 or n >= k + maxPts:
        return 1.0
    dp = [0.0] * (n + 1)
    dp[0] = 1.0
    s = 1.0
    for i in range(1, n + 1):
        dp[i] = s / maxPts
        if i < k:
            s += dp[i]
        if i - maxPts >= 0:
            s -= dp[i - maxPts]
    return sum(dp[k:])

# Example usage:
print(new21Game(10, 1, 10))  # Output: 1.0
print(new21Game(6, 1, 10))   # Output: 0.6
