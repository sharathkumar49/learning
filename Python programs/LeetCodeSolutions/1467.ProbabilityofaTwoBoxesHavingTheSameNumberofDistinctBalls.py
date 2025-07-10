"""
LeetCode 1467. Probability of a Two Boxes Having The Same Number of Distinct Balls

Given 2n balls of k different colors, return the probability that two boxes have the same number of distinct colors after dividing the balls equally.

Constraints:
- 1 <= k <= 8
- 1 <= balls[i] <= 6
- sum(balls) is even and 2 <= sum(balls) <= 16

Example:
Input: balls = [1,1]
Output: 1.0
"""
def getProbability(balls):
    from math import comb
    from functools import lru_cache
    n = sum(balls) // 2
    k = len(balls)
    total = 0
    valid = 0
    @lru_cache(None)
    def dfs(i, left, right, c1, c2):
        nonlocal total, valid
        if i == k:
            if left == right == n:
                total += 1
                if c1 == c2:
                    valid += 1
            return
        for l in range(balls[i]+1):
            r = balls[i] - l
            dfs(i+1, left+l, right+r, c1+(l>0), c2+(r>0))
    dfs(0,0,0,0,0)
    return valid/total

# Example usage:
balls = [1,1]
print(getProbability(balls))  # Output: 1.0
