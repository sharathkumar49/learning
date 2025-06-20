"""
879. Profitable Schemes

There are G members in a gang and a list of crimes. Each crime i has a profit[i] and requires group[i] members. Return the number of schemes to achieve at least P profit with at most G members.

Example 1:
Input: G = 5, P = 3, group = [2,2], profit = [2,3]
Output: 2

Example 2:
Input: G = 10, P = 5, group = [2,3,5], profit = [6,7,8]
Output: 7

Constraints:
- 1 <= G <= 100
- 0 <= P <= 100
- 1 <= group.length == profit.length <= 100
- 1 <= group[i] <= G
- 0 <= profit[i] <= 100
"""
def profitableSchemes(G, P, group, profit):
    MOD = 10**9 + 7
    dp = [[0] * (P+1) for _ in range(G+1)]
    dp[0][0] = 1
    for g, p in zip(group, profit):
        for i in range(G, g-1, -1):
            for j in range(P, -1, -1):
                dp[i][j] = (dp[i][j] + dp[i-g][max(0, j-p)]) % MOD
    return sum(dp[i][P] for i in range(G+1)) % MOD

# Example usage:
print(profitableSchemes(5, 3, [2,2], [2,3]))  # Output: 2
print(profitableSchemes(10, 5, [2,3,5], [6,7,8]))  # Output: 7
