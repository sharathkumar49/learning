"""
920. Number of Music Playlists
https://leetcode.com/problems/number-of-music-playlists/

Return the number of possible playlists of length goal that can be made from n different songs. Each song must be played at least once, and a song can only be played again if at least k other songs have been played.
Return the answer modulo 10^9 + 7.

Constraints:
- 0 <= k < n <= 100
- 1 <= goal <= 100

Example:
Input: n = 3, goal = 3, k = 1
Output: 6
"""
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (n+1) for _ in range(goal+1)]
        dp[0][0] = 1
        for i in range(1, goal+1):
            for j in range(1, n+1):
                dp[i][j] = (dp[i-1][j-1] * (n-j+1)) % MOD
                if j > k:
                    dp[i][j] = (dp[i][j] + dp[i-1][j] * (j-k)) % MOD
        return dp[goal][n]

# Example usage
if __name__ == "__main__":
    n = 3
    goal = 3
    k = 1
    print(Solution().numMusicPlaylists(n, goal, k))  # Output: 6
