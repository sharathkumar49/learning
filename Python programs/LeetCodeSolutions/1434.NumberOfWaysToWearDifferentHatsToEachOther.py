"""
LeetCode 1434. Number of Ways to Wear Different Hats to Each Other

There are n people and 40 types of hats. Each person may wear any subset of hats. Return the number of ways that all the people can wear different hats. Since the answer may be large, return it modulo 10^9 + 7.

Constraints:
- 1 <= n <= 10
- hats[i] is a list of hats that person i can wear

Example:
Input: hats = [[3,4],[4,5],[5]]
Output: 1
"""
def numberWays(hats):
    MOD = 10**9+7
    n = len(hats)
    from collections import defaultdict
    hat2people = defaultdict(list)
    for p, hs in enumerate(hats):
        for h in hs:
            hat2people[h].append(p)
    dp = [0]*(1<<n)
    dp[0] = 1
    for h in range(1, 41):
        ndp = dp[:]
        for mask in range(1<<n):
            for p in hat2people[h]:
                if not (mask & (1<<p)):
                    ndp[mask | (1<<p)] = (ndp[mask | (1<<p)] + dp[mask]) % MOD
        dp = ndp
    return dp[(1<<n)-1]

# Example usage:
hats = [[3,4],[4,5],[5]]
print(numberWays(hats))  # Output: 1
