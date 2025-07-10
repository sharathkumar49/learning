"""
LeetCode 1735. Count Ways to Make Array With Product

Given an array queries, for each query [n, k], return the number of ways to fill an array of length n with positive integers so that the product is k.

Example 1:
Input: queries = [[2,6],[5,1],[73,660]]
Output: [4,1,50734910]

Constraints:
- 1 <= queries.length <= 10^4
- 1 <= n, k <= 10^4
"""
MOD = 10**9 + 7
from math import comb

def waysToFillArray(queries):
    def prime_factors(x):
        d = 2
        factors = {}
        while d * d <= x:
            while x % d == 0:
                factors[d] = factors.get(d, 0) + 1
                x //= d
            d += 1
        if x > 1:
            factors[x] = factors.get(x, 0) + 1
        return factors
    res = []
    for n, k in queries:
        factors = prime_factors(k)
        ans = 1
        for cnt in factors.values():
            ans = ans * comb(cnt + n - 1, n - 1) % MOD
        res.append(ans)
    return res

# Example usage:
# queries = [[2,6],[5,1],[73,660]]
# print(waysToFillArray(queries))  # Output: [4,1,50734910]
