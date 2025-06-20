"""
940. Distinct Subsequences II
https://leetcode.com/problems/distinct-subsequences-ii/

Given a string s, return the number of distinct non-empty subsequences of s. Since the answer may be very large, return it modulo 10^9 + 7.

Constraints:
- 1 <= s.length <= 2000
- s consists of lowercase English letters.

Example:
Input: s = "abc"
Output: 7
"""
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = [0] * 26
        for c in s:
            idx = ord(c) - ord('a')
            total = sum(dp) % MOD
            dp[idx] = (total + 1) % MOD
        return sum(dp) % MOD

# Example usage
if __name__ == "__main__":
    s = "abc"
    print(Solution().distinctSubseqII(s))  # Output: 7
