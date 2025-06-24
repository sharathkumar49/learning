"""
1140. Stone Game II

Alice and Bob continue their games with piles of stones. There are several piles arranged in a row, and each pile has a positive integer number of stones. The game starts with Alice, and the number of piles is even.

A player can take all the stones in the first X remaining piles, where 1 <= X <= 2M. After taking these, the value of M is updated to max(M, X). The game continues until all the stones have been taken.

Return the maximum number of stones Alice can get.

Constraints:
- 1 <= piles.length <= 100
- 1 <= piles[i] <= 10^4

Example:
Input: piles = [2,7,9,4,4]
Output: 10

"""
def stoneGameII(piles):
    from functools import lru_cache
    n = len(piles)
    suffix = [0]*(n+1)
    for i in range(n-1, -1, -1):
        suffix[i] = suffix[i+1] + piles[i]
    @lru_cache(None)
    def dp(i, M):
        if i >= n:
            return 0
        res = 0
        for X in range(1, 2*M+1):
            if i+X > n:
                break
            res = max(res, suffix[i] - dp(i+X, max(M, X)))
        return res
    return dp(0, 1)

# Example usage
if __name__ == "__main__":
    print(stoneGameII([2,7,9,4,4]))  # Output: 10
