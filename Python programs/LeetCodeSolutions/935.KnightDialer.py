"""
935. Knight Dialer
https://leetcode.com/problems/knight-dialer/

The chess knight has a unique movement, and can move to eight positions from each square. Given an integer n, return how many distinct phone numbers of length n can be dialed.
You are allowed to place the knight on any numeric key, and the knight makes n-1 hops. Each hop must be a valid knight move.
Return the answer modulo 10^9 + 7.

Constraints:
- 1 <= n <= 5000

Example:
Input: n = 1
Output: 10
"""
class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        moves = {0: [4,6], 1: [6,8], 2: [7,9], 3: [4,8], 4: [0,3,9],
                 5: [], 6: [0,1,7], 7: [2,6], 8: [1,3], 9: [2,4]}
        dp = [1]*10
        for _ in range(n-1):
            ndp = [0]*10
            for i in range(10):
                for j in moves[i]:
                    ndp[j] = (ndp[j] + dp[i]) % MOD
            dp = ndp
        return sum(dp) % MOD

# Example usage
if __name__ == "__main__":
    n = 1
    print(Solution().knightDialer(n))  # Output: 10
