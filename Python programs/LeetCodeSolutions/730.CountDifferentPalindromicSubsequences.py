"""
LeetCode 730. Count Different Palindromic Subsequences

Given a string s, return the number of different non-empty palindromic subsequences in s. Since the answer may be very large, return it modulo 10^9 + 7.

Example 1:
Input: s = "bccb"
Output: 6

Example 2:
Input: s = "abcd"
Output: 4

Constraints:
- 1 <= s.length <= 1000
- s[i] is in {'a', 'b', 'c', 'd'}
"""
def countPalindromicSubsequences(s: str) -> int:
    MOD = 10**9 + 7
    n = len(s)
    dp = [[0]*n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for sz in range(2, n+1):
        for i in range(n-sz+1):
            j = i+sz-1
            if s[i] == s[j]:
                l, r = i+1, j-1
                while l <= r and s[l] != s[i]: l += 1
                while l <= r and s[r] != s[j]: r -= 1
                if l > r:
                    dp[i][j] = dp[i+1][j-1]*2 + 2
                elif l == r:
                    dp[i][j] = dp[i+1][j-1]*2 + 1
                else:
                    dp[i][j] = dp[i+1][j-1]*2 - dp[l+1][r-1]
            else:
                dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]
            dp[i][j] = (dp[i][j] + MOD) % MOD
    return dp[0][n-1]

# Example usage
if __name__ == "__main__":
    print(countPalindromicSubsequences("bccb"))  # Output: 6
    print(countPalindromicSubsequences("abcd"))  # Output: 4
