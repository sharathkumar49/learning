"""
LeetCode 1444. Number of Ways of Cutting a Pizza

Given a rectangular pizza represented as a string array, return the number of ways to cut the pizza into k pieces such that each piece contains at least one apple. Return the answer modulo 10^9 + 7.

Constraints:
- 1 <= rows, cols <= 50
- 1 <= k <= 10
- pizza[i][j] is 'A' (apple) or '.' (empty)

Example:
Input: pizza = ["A..","AAA","..."], k = 3
Output: 3
"""
def ways(pizza, k):
    MOD = 10**9+7
    rows, cols = len(pizza), len(pizza[0])
    apples = [[0]*(cols+1) for _ in range(rows+1)]
    for i in range(rows-1, -1, -1):
        for j in range(cols-1, -1, -1):
            apples[i][j] = (pizza[i][j] == 'A') + apples[i+1][j] + apples[i][j+1] - apples[i+1][j+1]
    from functools import lru_cache
    @lru_cache(None)
    def dp(i, j, cuts):
        if apples[i][j] == 0:
            return 0
        if cuts == 0:
            return 1
        res = 0
        for x in range(i+1, rows):
            if apples[i][j] - apples[x][j] > 0:
                res = (res + dp(x, j, cuts-1)) % MOD
        for y in range(j+1, cols):
            if apples[i][j] - apples[i][y] > 0:
                res = (res + dp(i, y, cuts-1)) % MOD
        return res
    return dp(0, 0, k-1)

# Example usage:
pizza = ["A..","AAA","..."]
k = 3
print(ways(pizza, k))  # Output: 3
