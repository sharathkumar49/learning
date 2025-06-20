"""
799. Champagne Tower

We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2, and so on. Each glass holds one cup of champagne. When poured, excess champagne spills equally to the two glasses below. Given poured, query_row, and query_glass, return the amount of champagne in that glass.

Example 1:
Input: poured = 1, query_row = 1, query_glass = 1
Output: 0.0

Example 2:
Input: poured = 2, query_row = 1, query_glass = 1
Output: 0.5

Constraints:
- 0 <= poured <= 10^9
- 0 <= query_row < 100
- 0 <= query_glass <= query_row
"""
def champagneTower(poured, query_row, query_glass):
    dp = [[0] * (k+1) for k in range(query_row+2)]
    dp[0][0] = poured
    for r in range(query_row+1):
        for c in range(r+1):
            excess = (dp[r][c] - 1) / 2.0
            if excess > 0:
                dp[r+1][c] += excess
                dp[r+1][c+1] += excess
    return min(1, dp[query_row][query_glass])

# Example usage:
print(champagneTower(1, 1, 1))  # Output: 0.0
print(champagneTower(2, 1, 1))  # Output: 0.5
