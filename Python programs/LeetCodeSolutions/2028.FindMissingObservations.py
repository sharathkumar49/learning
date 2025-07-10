"""
LeetCode 2028. Find Missing Observations

Given an array rolls, an integer mean, and the number of missing observations n, return an array representing the missing observations.

Example:
Input: rolls = [3,2,4,3], mean = 4, n = 2
Output: [6,6]

Constraints:
- 1 <= rolls.length, n <= 10^5
- 1 <= rolls[i], mean <= 6
"""

def missingRolls(rolls, mean, n):
    m = len(rolls)
    total = mean * (m + n) - sum(rolls)
    if total < n or total > 6 * n:
        return []
    q, r = divmod(total, n)
    res = [q] * n
    for i in range(r):
        res[i] += 1
    return res

# Example usage:
# print(missingRolls([3,2,4,3], 4, 2))  # Output: [6,6]
