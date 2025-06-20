"""
1000. Minimum Cost to Merge Stones
https://leetcode.com/problems/minimum-cost-to-merge-stones/

There are n piles of stones arranged in a row. The ith pile has stones[i] stones. A move consists of merging exactly k consecutive piles into one pile, and the cost is the total number of stones in those k piles. Return the minimum cost to merge all piles into one pile. If it is impossible, return -1.

Constraints:
- 3 <= stones.length <= 30
- 2 <= k <= 30
- 1 <= stones[i] <= 100

Example:
Input: stones = [3,2,4,1], k = 2
Output: 20
"""
from typing import List

class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n-1) % (k-1):
            return -1
        prefix = [0] * (n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + stones[i]
        dp = [[0]*n for _ in range(n)]
        for m in range(k, n+1):
            for i in range(n-m+1):
                j = i+m-1
                dp[i][j] = min(dp[i][mid] + dp[mid+1][j] for mid in range(i, j, k-1))
                if (m-1) % (k-1) == 0:
                    dp[i][j] += prefix[j+1] - prefix[i]
        return dp[0][n-1]

# Example usage
if __name__ == "__main__":
    stones = [3,2,4,1]
    k = 2
    print(Solution().mergeStones(stones, k))  # Output: 20
